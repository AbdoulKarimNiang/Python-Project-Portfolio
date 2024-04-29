import polars as pl

##### Paths ####
hired_employees_path = r"C:\Users\karim\Downloads\hired_employees.csv"
department_path = r"C:\Users\karim\Downloads\departments.csv"
job_path = r"C:\Users\karim\Downloads\jobs.csv"

### Schemas ####
employees_schema = {"id": pl.UInt16,
                    "name": pl.String,
                    "date_time": pl.String,
                    "department_id": pl.UInt8,
                    "job_id": pl.UInt8
                    }

department_schema = {"id": pl.UInt8,
                     "product_management": pl.String
                     }

job_schema = {"id": pl.UInt16,
              "job": pl.String
              }

### Employee Reading ###

employees_df = pl.read_csv(source=hired_employees_path, separator=",", schema=employees_schema)

print(f'Employee table columns after reading: {employees_df.columns}')

print(f'Employee table schema after reading: {employees_df.schema}')

employees_df = employees_df.with_columns(pl.col("date_time").str.to_datetime("%Y-%m-%dT%H:%M:%SZ"))

employees_df = employees_df.with_columns(
    date = pl.col("date_time").dt.date(),
    year=pl.col("date_time").dt.year().cast(pl.UInt16),
    time=pl.col("date_time").dt.time()
) \
    .drop("date_time")

print(f'Final Employee table schema: {employees_df.schema}')

### Deparment Reading ###

department_df = pl.read_csv(source=department_path, separator=",", schema=department_schema)
print(f'Department table columns after reading:{department_df.columns}')
print(f'Final Department table schema: {department_df.schema}')

### Job Reading ###

job_df = pl.read_csv(source=job_path, separator=",", schema=job_schema)

print(f'Job table columns after reading:{job_df.columns}')

print(f'Final Job table schema: {job_df.schema}')

# Write Pandas DataFrame to SQL Server
# employees_df.write_database(table_name='employee', connection=conn_str, if_table_exists='append')

# print(conn_str)
