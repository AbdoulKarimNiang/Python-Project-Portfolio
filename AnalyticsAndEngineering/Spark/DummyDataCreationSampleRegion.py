from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, udf
from pyspark.sql.types import StringType, IntegerType, DoubleType, DateType, TimestampType
import random
from datetime import datetime, timedelta
from time import time

start_time = time()

# Initialize Spark session
spark = SparkSession.builder.appName("DummyDataCreation").getOrCreate()

# Define Italian regions
regions = ["Abruzzo", "Basilicata", "Calabria", "Campania", "Emilia-Romagna", "Friuli Venezia Giulia", "Lazio", "Liguria", "Lombardia", "Marche", "Molise", "Piemonte", "Puglia", "Sardegna", "Sicilia", "Toscana", "Trentino-Alto Adige", "Umbria", "Valle d'Aosta", "Veneto"]

# Generator function to produce consecutive dates
def generate_dates(start_date, num_days):
    for i in range(num_days):
        yield (start_date + timedelta(days=i)).strftime("%Y-%m-%d"),

# Start date
start_date = datetime.strptime("2020-01-01", "%Y-%m-%d")

# Generate 1 million consecutive dates
dates = generate_dates(start_date, 1000000)

# Create DataFrame from the generator
df = spark.createDataFrame(dates, ["date"])

# Function to generate random time
def generate_time():
    return datetime.strptime(f"{random.randint(0, 23)}:{random.randint(0, 59)}:{random.randint(0, 59)}", "%H:%M:%S")

# UDF for random time generation
time_udf = udf(generate_time, TimestampType())

# Function to generate random region
def generate_region():
    return random.choice(regions)

# UDF for random region generation
region_udf = udf(generate_region, StringType())

# Function to generate random latency
def generate_latency():
    return random.uniform(0, 100)

# UDF for random latency generation
latency_udf = udf(generate_latency, DoubleType())

# Function to generate random throughput
def generate_throughput():
    return random.uniform(10, 1000)

# UDF for random throughput generation
throughput_udf = udf(generate_throughput, DoubleType())

# Add additional columns to DataFrame
df = df.withColumn("region", region_udf())
df = df.withColumn("latency", latency_udf())
df = df.withColumn("throughput", throughput_udf())
df = df.withColumn("time", time_udf())

# Show the schema of the DataFrame
df.printSchema()

# Show some example rows
df.show(10)

# Optionally, write to a CSV file
# df.write.csv("dummy_data.csv", header=True)

# Stop Spark session
spark.stop()

end_time = time()

time_difference = start_time - end_time

print("The query lasted for {time_difference}") 

path = r"C:\Users\karim.niang\Downloads\ran_monitoring.parquet"
df.write.format("parquet").save(path)