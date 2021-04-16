import pandas as pd
dataku = pd.read_csv('retail_raw_reduced_data_quality.csv')
# Check kolom yang memiliki missing data
print('Check kolom yang memiliki missing data:')
print(dataku.isnull().any())

# Filling the missing value (imputasi)
print('\nFilling the missing value (imputasi):')
print(dataku['quantity'].fillna(dataku.quantity.mean()))

# Drop missing value
print('\nDrop missing value:')
print(dataku['quantity'].dropna())