from faker import Faker
import polars as pl
from random import randint

# locale is set to get Fake data specific
# to a determined region
fake = Faker(locale="it_IT")

occurances = 10

# List comprehension to create data in more efficient way
# than classic for loops
names = [fake.unique.name() for i in range(occurances+1)]
addresses = [fake.address() for i in range(occurances+1)]
cities = [fake.city() for i in range(occurances+1)]
ages = [randint(18, 96) for i in range(occurances+1)]

df_data = {
    'name': names,
    'age':ages,
    'address':addresses,
    'city':cities
}

df = pl.DataFrame(data= df_data)

# You can use the list modules on a column if it containes
# data of list type
df = df.with_columns(
    surname = pl.col("name").str.split(" ").list.last()
)

print(df)