import mysql.connector
from sqlalchemy import create_engine
import project_info
from data_cleaning import employees_df, department_df, job_df

config = {
    'host': project_info.host_name,
    'user': project_info.user_name,
    'password': project_info.password,
    'database': project_info.db_name
}

# Create MySQL connection
connection = mysql.connector.connect(**config)

# Create SQLAlchemy engine
engine = create_engine(
    f"mysql+mysqlconnector://{project_info.user_name}:{project_info.password}@{project_info.host_name}/{project_info.db_name}")

# Write DataFrames to database using SQLAlchemy engine
employees_df.write_database('employee', engine.url, if_table_exists='replace')
department_df.write_database('department', engine.url, if_table_exists='replace')
job_df.write_database('job', engine.url, if_table_exists='replace')

# Commit changes and close connections
connection.commit()
connection.close()
print("Tables inserted!")
