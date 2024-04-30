import os
import pandas as pd
import polars as pl

path = # inser the pat here
year = '2023'

schema = {
    'data': pl.String,
    'vendite': pl.UInt32,
    'fatturato': pl.Float64,
}

combined_df = pl.DataFrame()

for root, directory, files in os.walk(path):
    for file in files:
        path = os.path.join(root, file)
        month = os.path.basename(root)
        year_month = year + month
        if file.endswith('.csv'):
            correct_file = file.replace('.csv', "")
        df = pl.read_csv(path, schema=schema)
        df = df.with_columns(
            anno_mese=pl.lit(year_month),
            file=pl.lit(correct_file)
        )
        combined_df = pl.concat([combined_df, df])

print(combined_df.shape)
subeset = ['data', 'vendite', 'fatturato']

combined_df.unique(subset=subeset)

print(combined_df.shape)

df = combined_df.to_pandas()

filter_cond = df.duplicated()

df = df[filter_cond]

print(df)
