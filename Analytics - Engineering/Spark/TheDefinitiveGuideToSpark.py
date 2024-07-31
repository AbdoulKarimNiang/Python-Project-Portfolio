#  °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°° Chapter 6. Working with different data types °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

# General Import
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DecimalType, DateType

# Import for string
from pyspark.sql.functions import (col, instr, lit, bround, round, expr, corr, monotonically_increasing_id, initcap,
                                   lower, upper, translate)
# Import for dates
from pyspark.sql.functions import (current_date, current_timestamp, date_add, date_sub,
                                   date_diff, hour, to_date, regexp_replace, months_between, to_timestamp,
                                   unix_timestamp, from_unixtime)

# Import for Nulls
from pyspark.sql.functions import (ifnull, coalesce, nullif, nvl, nvl2)

# Import complex data types

from pyspark.sql.functions import struct, any_value, split, size, array_size, get_json_object, json_tuple

# Import for aggregations
from pyspark.sql.functions import sum, max, min, count, avg, std, variance, approx_count_distinct

spark6 = SparkSession.builder.appName(
    "The Definitive Guide: Working with different data types").enableHiveSupport().getOrCreate()

myschema = StructType([
    StructField("InvoiceNo", StringType(), nullable=True),
    StructField("StockCode", StringType(), nullable=True),
    StructField("Description", StringType(), nullable=True),
    StructField("Quantity", DecimalType(4, 2), nullable=True),
    StructField("InvoiceDate", DateType(), nullable=True),
    StructField("UnitPrice", DecimalType(6, 2), nullable=True),
    StructField("CustomerID", StringType(), nullable=True),
    StructField("Country", StringType(), nullable=True),
])

path_retail_2010_12_01 = r"C:\Users\karim\PycharmProjects\PythonProject\Spark-The-Definitive-Guide\data\retail-data\by-day\2010-12-01.csv"

retail_2010_12_01 = spark6.read.format("csv").option("header", True).schema(myschema).load(path_retail_2010_12_01)

retail_2010_12_01.createOrReplaceTempView("retail_2010_12_01")

retail_2010_12_01.printSchema()

# Filtering data
# print("Filtering data data have InvoiceNo equal to 536365 ")
# retail_2010_12_01.where(col("InvoiceNo") == "536365").show()
# retail_2010_12_01.where("InvoiceNo = 536365").show()

# print("Filtering data data have InvoiceNo that is not equal to 536365 ")
# retail_2010_12_01.where(col("InvoiceNo") != 536365).show(5)
# retail_2010_12_01.where("InvoiceNo <> 536365").show(5)
# retail_2010_12_01.where("InvoiceNo != 536365").show(5)

# print(fr"Using Multiple conditions with 'AND' 'OR")
# price_condition = col("UnitPrice") > 600.00
# description_condition = instr("Description", "POSTAGE") >= 1
# DotCode_condition = col("StockCode").isin("DOT")
# retail_2010_12_01.where(DotCode_condition).where(price_condition | description_condition).show()

# print("Boolean also in withColumns")

# (retail_2010_12_01 \
#    .withColumn("isExpensive", DotCode_condition & (price_condition | description_condition)) \
#    .where("isExpensive")
#    .show())

## Working with numbers

# Calculate the power

# retail_2010_12_01 \
#    .select(
#        col("Quantity"),
#        (pow(col("Quantity") * col("UnitPrice"), 2) + 5)
#            .alias("FabricatedQuantity")
#    ).show(2)

# print("SQL Version Fabricated Quantity")
# spark6.sql("SELECT POW((Quantity * UnitPrice),2) + 5 as FabricatedQuantity FROM retail_2010_12_01").show(2)

# Rounding
# Using and Empty Rdd that is converted to DF doesn't work because the Select and WithColumn can't iterate over it
# empty_rdd = spark6.sparkContext.emptyRDD()

# empty_schema = StructType([])

# df = empty_rdd.toDF(schema=empty_schema)

# df.show()

# Not working to created a lit column and convert it.

# df \
#    .select(expr(round(lit("2.5").cast(DecimalType(3, 1)))).alias("Rounded") \
#            , expr(bround(lit("2.5").cast(DecimalType(3, 1))).alias("Brounded"))) \
#    .show()


# Calculating the correlation between Quantity and UnitrPirce
# retail_2010_12_01.select(corr("Quantity", "UnitPrice")).show()

# Describe

# retail_2010_12_01.describe().show()


# MonoliticalID

# retail_2010_12_01.select(col("*"),monotonically_increasing_id().alias("ID")).show(10)


## Working with Strings

# retail_2010_12_01.select(
#    initcap(col("Description").alias("init_description")),
#    upper(col("Description").alias("cap_description")),
#    lower(col("Description").alias("lower_description"))
# ).show(5)

# print("Init with SQL")
# spark6.sql("""
# Select initcap(Description) as init_description,
# upper(Description) as cap_description,
# lower(Description) as low_description
# from retail_2010_12_01 LIMIT 2""") \
#    .show()


# Regex

# regex_string = "BLACK|WHITE|GREEN|BLUE"

# retail_2010_12_01 \
#    .select(regexp_replace(col("Description"), regex_string, "COLOR")) \
#    .show(10,False)


# Multiple characters replace with translate

# retail_2010_12_01 \
#    .select(translate("Description", "LEEF", "1337")).alias("Translate") \
#    .show(5)


## DateTime Zones

dfDate = spark6.range(1)

# dfDate \
#    .select(current_date().alias("Today"),
#    current_timestamp().alias("Now"),
#    date_sub("today",7).alias("Lastweek"),
#    date_add("today", 7).alias("Futureweek"),
#    date_diff("futureweek","today").alias("DaysDifference"),
#    to_date(lit("2020-01-15"), "yyyy-MM-dd")
#    ) \
#    .show(truncate=False)

# dfDate.select(to_date(lit("2020-01-30")).alias("start"),
#                      to_date(lit("2020-06-30")).alias("end"),
#             months_between("end", "start").alias("month difference")).show()

## Working with Nulls

# Filter Nulls
# (retail_2010_12_01 \
# .where(col("Description").isNull())
# .show(5)
# )

# retail_2010_12_01.select(coalesce(col("Description"), col("CustomerID"))).show(20, False)


# (retail_2010_12_01.select(
#    coalesce("Description", "CustomerID").alias("Coalesce"),
#    ifnull("Description", "CustomerID").alias("IffNull"),
#    nullif(retail_2010_12_01.Description, retail_2010_12_01.Country).alias("NullIf"),
#    nvl("Description", "CustomerID").alias("Nvl"),
#    nvl2("Description", "CustomerID", "Country").alias("Nvl2")
# ) \
#    .where(col("Description").eqNullSafe(None)) \
# .show(20, False))


# spark6.sql("""SELECT DESCRIPTION,
#           NULLIF(Description, CustomerID)
#           FROM retail_2010_12_01 where Description is null
#           """).show(20,False)


# Dropping Nulls

# na.drop
# before = retail_2010_12_01.count()
# after = retail_2010_12_01.na.drop(how='any').count()
# rows_deleted = before - after
# print(f"Number rows deleted: {rows_deleted}")

# dropna using pandas
# retail_pandas = retail_2010_12_01.toPandas()
# before_na = len(retail_2010_12_01.columns)
# ratail_drop_na = retail_pandas.dropna(axis='columns', how='any')

# after_na = len(ratail_drop_na.columns)
# print(f"columns dropped: {before_na - after_na}")

# Fill na

## Get the rows where description is null with a safe comparison
# retail_2010_12_01.where(col("Description").eqNullSafe(None)).show(5)

## Dictionary mapping
# fill_mapping = {"Description": "Unknown", "CustomerID": "ABx305"}


## Filter condition with pipe
# filter_condition = ((col("Description") == "Unknown") | (col("StockCode") == "ABx305"))

## Fill-up with the dictionary mapping
# retail_2010_12_01.fillna(
#    fill_mapping) \
#    .where(filter_condition) \
#    .show(5, False)

## Ordering Data
# using desc_nulls_last
# retail_2010_12_01 \
#    .select("InvoiceNo", "Description", "Quantity") \
#    .groupBy("InvoiceNo", "Description").agg(sum("Quantity").alias("Quantity")) \
#    .orderBy([col("InvoiceNo").asc_nulls_first(), col("Description").desc_nulls_first(), col("Quantity").desc_nulls_last()]) \
#    .show(30, False)

# Working with Complex data types

# struct_df = retail_2010_12_01 \
#    .selectExpr("struct(Description,InvoiceNo)").alias("StructColumn") \
#     .show(20, False)

# retail_2010_12_01 \
#    .select(struct("Description", "InvoiceNo").alias("STRUCT")) \
#    .select("STRUCT.*") \
#    .show(20, False)

## Splitting
# retail_2010_12_01.select(size(split("Description", " "))).show(20, False)
# retail_2010_12_01.select(array_size(split("Description", " "))).show(20, False)

##Woring with JSON

# Json_df = spark6.range(1).selectExpr("""
#    '{"MyJsonKey":{"MyJsonValue":[1,2,3]}}' as JsonString""")

# (Json_df.select(
#    get_json_object(col("JsonString"), "$.MyJsonKey.MyJsonValue"[0]),
#    json_tuple(col("JsonString"),"MyJsonKey")) \
# .show(truncate=False))

# Using UDF
# Not working
# from pyspark.sql.functions import udf


# def power3(colonna) -> int:
#    return colonna ** 3


# power3udf = udf(power3, DecimalType())

# retail_2010_12_01 \
#    .select("Quantity", power3udf(col("Quantity")).alias("QuantityCubed")) \
#    .show(3, False)


#  °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°° Chapter 7. Aggregations °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
spark6.stop()

spark7 = SparkSession.builder.appName(
    "Chapter 7").enableHiveSupport().getOrCreate()

path_all_csv = r"C:\Users\karim\PycharmProjects\PythonProject\Spark-The-Definitive-Guide\data\retail-data\all\online-retail-dataset.csv"

myschema_chp7 = StructType([
    StructField("InvoiceNo", StringType(), nullable=True),
    StructField("StockCode", StringType(), nullable=True),
    StructField("Description", StringType(), nullable=True),
    StructField("Quantity", DecimalType(4, 2), nullable=True),
    StructField("InvoiceDate", StringType(), nullable=True),
    StructField("UnitPrice", DecimalType(6, 2), nullable=True),
    StructField("CustomerID", StringType(), nullable=True),
    StructField("Country", StringType(), nullable=True),
])

retail_all_csv = spark7 \
    .read \
    .format("csv") \
    .option("header", True) \
    .option("inferSchema", True) \
    .load(path=path_all_csv) \
    .coalesce(5)

from pyspark.sql.functions import  to_timestamp
retail_all_csv = retail_all_csv \
    .withColumn("InvoiceDate",  to_timestamp("InvoiceDate", format="M/d/y HH:mm")) \
    .where(col("InvoiceDate").isNotNull())

retail_all_csv.cache()
retail_all_csv.show()
retail_all_csv.createOrReplaceTempView("retail_all")

# print("Total Rows:")
# total_rows = retail_all_csv.count()
# print("Total Rows Colum")
# retail_all_csv.select(count("StockCode").alias("CountStockCode"))
# print("Approximate Distinct Count")
# retail_all_csv.select(approx_count_distinct("StockCode", rsd=0.05).alias("DistinctCount"))
