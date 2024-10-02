from faker import Faker
import polars as pl
from datetime import datetime
import pyarrow
from time import time

start = time()


today = datetime.today().year


# locale is set to get Fake data specific
# to a determined region
fake = Faker(locale="it_IT")

occurances = 1_000_000 + 1 

# List comprehension to create data in more efficient way
# than classic for loops
df_data = {
    'name': [fake.first_name() for i in range(occurances)],
    'surname': [fake.last_name() for i in range(occurances)],
    'job': [fake.job() for i in range(occurances)],
    'date_of_birth':[fake.date_of_birth() for i in range(occurances)],
    'full_address':[fake.address() for i in range(occurances)],
    'city':[fake.city() for i in range(occurances)],
    'phone_number': [fake.phone_number() for i in range(occurances)],
}


df = pl.DataFrame(data= df_data)

# You can use the list modules on a column if it containes
# data of list type

pl.Config(fmt_str_lengths=50)

df = df.with_columns(
    age = pl.lit(today) - pl.col('date_of_birth').dt.year(),
    year = pl.col("date_of_birth").dt.year(),
    month = pl.col("date_of_birth").dt.month(),
    day = pl.col("date_of_birth").dt.day(),
    province = pl.col('full_address').str.extract( r'\(([A-Z]{2})\)'),
    comune = pl.col('full_address').str.extract(r'\d{5},\s*(.*?)\s*\([A-Z]{2}\)'),
    postal_code = pl.col("full_address").str.extract(r'(\d{5})', 0)
)

print(df)

end = time()

duration = end - start

print(f"The code took: {duration}")