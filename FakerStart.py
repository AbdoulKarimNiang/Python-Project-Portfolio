from faker import Faker
from collections import Counter
import polars as pl
from random import randint

fake = Faker(locale="it_IT")

occurances = 10

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

df = df.with_columns(
    surname = pl.col("name").str.split(" ").list.last()
)

print(df.head())