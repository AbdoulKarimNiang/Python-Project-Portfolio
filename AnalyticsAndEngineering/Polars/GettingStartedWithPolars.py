import polars as pl

file_path = r'C:\**\**\Downloads\foods.csv'

dtypes = {
    "category": str,
    "calories": float,
    "fats_g": float,
    "sugars_g": int
}

# loading the data
df = pl.read_csv(file_path, has_header=True, dtypes=dtypes)
# A better way to load the data is using scan_csv to make it lazy and allow fully benefit from the
# Polars optimization

# # Get some basic information
# print("Getting some basic information")
# print(df.describe())
# print(df.sample(5))
# for column, data_type in zip(df.columns, df.dtypes):
#     print(f"{column}: {data_type}")
#
# # Select columns and information
# print(f"Two ways of printing all columns")
# print(df.select(pl.all()))
# print(df.select(pl.col("*")))

# Select columns based on data types
print("Selecting the float data types")
print(df.select(pl.selectors.float()))
print("Selecting the string data types")
print(df.select(pl.selectors.string()))
print("Selecting the integer data types")
print(df.select(pl.selectors.integer()))
print("Selecting the numeric data types")
print(df.select(pl.selectors.numeric()))
print("Selecting the numeric data types")
print(df.select(pl.selectors.numeric()))
print("Selecting all not numeric data types")
print(df.select(~pl.selectors.numeric()))


# # Performing some basic operation
# print(df.select(
#     (pl.col("calories") + 5).alias("calories +5"),
#     (pl.col("fats_g") + 3.5).alias("fats_g +3.5")
# ))
#
# # Creating new columns
# print(df.with_columns(
#     (pl.col("calories") + 5).alias("calories +5"),
#     (pl.col("fats_g") + 3.5).alias("fats_g +3.5")
# ))
