import tabula
import polars as pl
from functools import reduce
import os

# File path
file = "2023_Estratto_conto_annuale.pdf"
base_path = os.path.expanduser("~")
path = os.path.join(base_path,"Downloads", file)


df_list = tabula.read_pdf(path, pages='1-2,4-6,8-14,16-23', stream=True, pandas_options={'header': True})



def process_dtaframe(df):
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

    if df.columns < 5:
        schema = {
            "date_operation": pl.String,
            "data_valuta": pl.Date,
            "exits": pl.Float32,
            'description': pl.String
          }
    elif df.columns == 5:
        schema = {
            "date_operation": pl.String,
            "data_valuta": pl.Date,
            "exits": pl.Float32,
            "incomes": pl.Float32,
            'description': pl.String
        }

    df = pl.from_pandas(df, schema_overrides=schema)




df = pl.DataFrame()

polars_dataframes = [pl.from_pandas(df_list[i], schema_overrides=schema) for i in range(1, len(df_list))]

print(polars_dataframes)

# df = reduce(lambda x, y: pl.concat([x, y]), polars_dataframes, df)

# print(df)
