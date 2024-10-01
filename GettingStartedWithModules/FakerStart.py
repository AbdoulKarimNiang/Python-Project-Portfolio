from faker import Faker
import polars as pl
from datetime import datetime

today = datetime.today().year


# locale is set to get Fake data specific
# to a determined region
fake = Faker(locale="it_IT")

occurances = 10

# List comprehension to create data in more efficient way
# than classic for loops
df_data = {
    'name': [fake.unique.first_name() for i in range(occurances+1)],
    'surname': [fake.last_name() for i in range(occurances+1)],
    'date_of_birth':[fake.date_of_birth() for i in range(occurances+1)],
    'full_address':[fake.address() for i in range(occurances+1)],
    'city':[fake.city() for i in range(occurances+1)],
    'phone_number': [fake.phone_number() for i in range(occurances+1)]
}

df = pl.DataFrame(data= df_data)

# You can use the list modules on a column if it containes
# data of list type

pl.Config(fmt_str_lengths=50)

df = df.with_columns(
    year = pl.lit(today) - pl.col('date_of_birth').dt.year(),
    province = pl.col('full_address').str.extract( r'\(([A-Z]{2})\)'),
    comune = pl.col('full_address').str.extract(r'\d{5},\s*(.*?)\s*\([A-Z]{2}\)'),
    cap = pl.col("full_address").str.extract(r'(\d{5})', 0)
)

print(df)