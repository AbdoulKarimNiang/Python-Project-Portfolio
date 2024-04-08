import pandas as pd

closure = '022024'
folder = closure[2:] + "." + closure[:2]

path = rf"U:\**\**-**\0**\**\{folder}\MovimentiCommessa{closure}.xlsx"

new_path = rf"U:\**\**-**\0**\**\{folder}\MovimentiCommessa{closure}LV-FV.xlsx"

dtype = {
    "Competenza": 'str',
    "Tipo": "category",
    "Nr.": "str",
    "Descrizione": "str",
    "Importo": "float",
    "Descrizione riga movimento": "str",
    "Nr. Documento": "str",
    "Data Documento": 'str',
    "Tipo Contropartita": "category",
    "Nome": "str",
    "Codice Commessa": "str",
    "Descrizione Commessa": "str",
    "Classificazione servizio": "category",
    "Switch Costo / Ricavo": "category",
    "Data Movimento Contabile": 'str',
    "Protocollo": "str",
    "AREA_GEO": "category",
    "TPCOM": "category"
}

mov_comm_com_df = pd.read_excel(path, dtype=dtype, header=2)

mov_comm_com_df[['Competenza', 'Data Documento', 'Data Movimento Contabile']] = (
    mov_comm_com_df[['Competenza', 'Data Documento', 'Data Movimento Contabile']]
    .apply(pd.to_datetime)
)
# Changing the value of ARTICOLO for LV - FV and LA
basic_criteria = \
    (
            mov_comm_com_df['Codice Commessa'].str.contains('-LV') |
                    mov_comm_com_df['Codice Commessa'].str.contains('-FV') |
                    mov_comm_com_df['Codice Commessa'].str.contains('-LA')
    )

criteria_other = (mov_comm_com_df['Tipo'] == 'Articolo') & ~ (basic_criteria  # tilda is used as it was a "not"
                    )
criteria_LV = (
            basic_criteria
        ) & (mov_comm_com_df['Tipo'] == 'Articolo')

print(mov_comm_com_df[mov_comm_com_df['Nr.'] == 'ACQ_LAV'].count())  ## print before changes
mov_comm_com_df.loc[criteria_LV, 'Nr.'] = 'ACQ_LAV'
mov_comm_com_df.loc[criteria_other, 'Nr.'] = 'ACQUISTI'

print(mov_comm_com_df[mov_comm_com_df['Nr.'] == 'ACQ_LAV'].count())  ## print after changes
# print(mov_comm_com_df.head(5))
print(mov_comm_com_df.sample(5))
mov_comm_com_df.loc[criteria_LV, 'Nr.'] = 'ACQ_LAV'

# Filer LV - FV
mov_comm_com_df = mov_comm_com_df[mov_comm_com_df['Codice Commessa'].str.contains('-LV|-FV')]

mov_comm_com_df.to_excel(new_path, index=False, startrow=0, startcol=0)



