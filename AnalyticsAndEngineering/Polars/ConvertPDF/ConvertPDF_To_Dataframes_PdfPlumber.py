import pdfplumber
import polars as pl
from functools import reduce
import os


# File path
file = "2023_Estratto_conto_annuale.pdf"
base_path = os.path.expanduser("~")
path = os.path.join(base_path,"Downloads", file)


with pdfplumber.open(path) as pdf:
    pages = pdf.pages
    for i in range(0, len(pages)):
        current_page = pages[i]
        table = current_page.extract_tables(table_settings={
            "vertical_strategy": "text",
            "horizontal_strategy":"text"
        })
        print(table)