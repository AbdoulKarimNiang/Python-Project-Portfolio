import tabula
import polars as pl
from functools import reduce
import os

# File path
file = "2023_Estratto_conto_annuale.pdf"
base_path = os.path.expanduser("~")
path = os.path.join(base_path,"Downloads", file)


df_list = tabula.read_pdf(path, pages='1-2,4-6,8-14,16-23', stream=True,
                          pandas_options={'header': True})

def process_dataframe(df):
    """
    The function remove columns with only null values and
    rows with null values.

    Generally the Bank statement will contain exist so the schema takes in consideration
    this thing.

    :param df: a pandas dataframe
    :return: a polars dataframe
    """

    df = df.dropna(axis='columns', how='all')
    df = df.dropna(axis ='index', how='all')

    if len(df.columns) < 5:
        schema = {
            "date_operation": pl.String,
            "date_valuta": pl.String,
            "spendings": pl.String,
            'description': pl.String
          }

        df_polars = pl.DataFrame(df, schema =schema)

        df_polars = df_polars.with_columns(incomes=pl.lit("0").cast(pl.Int8))

    elif len(df.columns) == 5:
        schema = {
            "date_operation": pl.String,
            "date_valuta": pl.String,
            "spendings": pl.String,
            "incomes": pl.String,
            'description': pl.String
        }

        df_polars = pl.DataFrame(df, schema =schema)

    df_polars = df_polars.filter(~pl.col("description").is_null())

    df_polars= df_polars.with_columns(
        spendings=pl.col("spendings")
            .cast(pl.Utf8)
            .str.replace_all(r"\.", "")  # Remove thousands separators (periods)
            .str.replace(",", ".")  # Replace comma with a period (decimal point)
            .str.replace_all(r"[^\d.]", "").cast(pl.Float32),
        incomes=pl.col("incomes").cast(pl.Utf8)
            .str.replace_all(r"\.", "")  # Remove thousands separators (periods)
            .str.replace(",", ".")  # Replace comma with a period (decimal point)
            .str.replace_all(r"[^\d.]", "").cast(pl.Float32)
    )

    df_polars = df_polars.with_columns(
        pl.col("date_operation").fill_null(strategy='forward'),
        pl.col("date_valuta").fill_null(strategy='forward'),
        pl.col("spendings").fill_null(value=0),
        pl.col('incomes').fill_null(value=0)
    )

    df_polars =df_polars.group_by("date_operation", "date_valuta").agg(
        pl.col("spendings"),
        pl.col("incomes"),
        pl.col("description").str.concat(delimiter=" ")
    )


    df_polars = df_polars.explode("spendings","incomes")

    # Cast "spendings" and "incomes" to Float32 to allow numeric operations
    df_polars = df_polars.with_columns(
        pl.col("spendings").cast(pl.Float32),
        pl.col("incomes").cast(pl.Float32)
    )

   # df_polars = df_polars.filter(
    #    pl.col("spendings") != 0 & pl.col("incomes") != 0
    #)


    #df_polars = df_polars.with_columns(
     #   date_operation=pl.col("date_operation").str.strptime(pl.Date,format="%d/%m/Y"),
      #  date_valuta=pl.col("date_valuta").str.strptime(pl.Date,format="%d/%m/Y"),
       # incomes=pl.col("incomes").str.extract(f"d+"),
        #spendings=pl.col("incomes").str.extract(f"d+")
    #)

    # df_polars = df.filter(pl.col("dat"))

    return df_polars

polars_dataframes = [process_dataframe(df_list[i]) for i in range(1, len(df_list))]

print(polars_dataframes)

# df = reduce(lambda x, y: pl.concat([x, y]), polars_dataframes, df)

# print(df)
