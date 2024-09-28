import camelot
import polars as pl
from functools import reduce
import os


# File path
file = "2023_Estratto_conto_annuale.pdf"
base_path = os.path.expanduser("~")
path = os.path.join(base_path,"Downloads", file)


tables = camelot.read_pdf(path)

print(tables)