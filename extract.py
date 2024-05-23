import pandas as pd


excel_file = 'logbook.xlsx'

sheet_name = 'Sheet1'

df = pd.read_excel(excel_file, sheet_name=sheet_name)

df['datetime']= pd.to_datetime(df['datetime'], format = '%d/%m/%Y %H:%M:%S')

df_15= df[df['datetime'].dt.hour == 15]
df_16= df[df['datetime'].dt.hour == 16]

data_15 = df_15[['datetime', 'date_column']].values
data_16 = df_16[['datetime', 'date_column']].values


with open('info_extraite.txt', 'w') as file:
    file.write('Données pour 15h : \n')
    for row in data_15:
        file.write(f"{row[0].strftime('%d/%m/%Y %H:%M:%S')} - {row[1]}\n")
    file.write('Données pour 16h: \n')
    for row in data_16:
        file.write(f"{row[0].strftime('%d/%m/%Y %H:%M:%S')} - {row[1]}\n")

print('Extraction terminée, vérifiez le fichier info_extraite.txt')
    