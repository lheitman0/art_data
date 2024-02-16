import pandas as pd

excel_data = pd.read_excel('data/catalog.xlsx')
excel_data.to_csv('data/art_data.csv', index = False)