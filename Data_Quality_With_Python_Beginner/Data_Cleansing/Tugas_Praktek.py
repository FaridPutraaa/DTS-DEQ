import pandas as pd
dataku = pd.read_csv('retail_raw_reduced_data_quality.csv')
print(dataku['item_price'].fillna(dataku['item_price'].mean()))