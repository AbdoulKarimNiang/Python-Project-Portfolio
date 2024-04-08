import pandas as pd

# loading data
file_path = r"U:\Rivoli\area-amministrazione\kniang\Contabilità\23-24\2024.02\MovimentiCommessaDDT_202402.xlsx"

dtype = {
    'Competenza': 'datetime64[ms]',  # it represents only date Date
    'Descrizione Commessa': str,
    'Codice Commessa': str,
    'Importo': float
}
mov_comm_ddt = pd.read_excel(file_path, usecols="A,E,L,M", dtype=dtype)

max_date = max(mov_comm_ddt.Competenza)
min_date = min(mov_comm_ddt.Competenza)

# Check the date ranges
print(f"The max date is {max_date}")
print(f"The max date is {min_date}")
description = mov_comm_ddt.describe()
count_row = description.loc['count']
count_value = count_row.astype(int).values[0]
print(mov_comm_ddt.describe())
print(count_value)
print(mov_comm_ddt.head(5))

# Create DDT number
string: list[str] = ["DDT-"] * count_value
start_range = 2300001
range_ddt = range(start_range, start_range + count_value + 1)

list_to_add = []
for ddt, number in zip(string, range_ddt):
    value = ddt + str(number)
    list_to_add.append(value)
print(list_to_add)

# Adding columns
mov_comm_ddt['Nr.Documento'] = list_to_add
mov_comm_ddt['Conto'] = 355001006
mov_comm_ddt['Descrizione'] = 'ACQUISTO MATERIALI DI MANUTENZIONE'

# Removing columns
del mov_comm_ddt["Competenza"]

# Reorder

desired_order = ["Conto", "Descrizione", "Nr.Documento", "Descrizione Commessa", "Codice Commessa","Importo"]

mov_comm_ddt = mov_comm_ddt[desired_order]

# Data to append
new_mov_mov_comm_ddt = mov_comm_ddt.copy()
new_mov_mov_comm_ddt.Importo *= -1
new_mov_mov_comm_ddt['Codice Commessa'] = ''

# Appending
df_appended = pd.concat([mov_comm_ddt, new_mov_mov_comm_ddt], ignore_index=False)

df_appended.sort_values(["Nr.Documento", "Importo"], ascending=False, inplace=True)


print(df_appended)

# save the file

new_path = r"U:\Rivoli\area-amministrazione\02. CONTROLLO DI GESTIONE\STAGIONE 23-24\2024.02\MovimentiCommessa022024_scritture.xlsx"

df_appended.to_excel(new_path, sheet_name='Sheet1', index=False, startrow=0, startcol=0)
