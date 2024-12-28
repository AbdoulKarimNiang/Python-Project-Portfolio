import polars as pl
from skrub import deduplicate
import typo  


area_types =  ['Nord-Ovest', 'Nord-Est', 'Centro','Sud', 'Isole']

area_types_missing = [ typo.StrErrer(i, seed=42).missing_char().result for i in  area_types for j in range (5) ] 

print(area_types_missing)