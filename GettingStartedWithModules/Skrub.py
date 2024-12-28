from skrub.datasets import make_deduplication_data
from skrub import deduplicate
from random import seed, randint
import polars as pl

area = ['Nord-East', 'Nord-West', 'Center', 'South', 'Islands']

occurances = [randint(100, 150) for i in range(len(area))]

seed = 42

area_corrupted = make_deduplication_data(
    examples=area,
    entries_per_example= occurances, 
    prob_mistake_per_letter= 0.02,
    random_state= seed 
)

area_sane = deduplicate(area_corrupted)

print(area_sane.__class__)


data = pl.DataFrame({
    'corrupted': area_corrupted,
    'clean' : area_sane
})

filtered = data.filter(
~ pl.col('corrupted').is_in(area)
)
    

print(filtered.sample(10))