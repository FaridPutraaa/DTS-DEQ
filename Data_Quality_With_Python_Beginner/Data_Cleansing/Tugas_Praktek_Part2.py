import pandas as pd
dataku = pd.read_csv('retail_raw_reduced_data_quality.csv')

# Q1, Q3, dan IQR
Q1 = dataku['item_price'].quantile(0.25)
Q3 = dataku['item_price'].quantile(0.75)
IQR = Q3 - Q1

# Check ukuran (baris dan kolom) sebelum data yang outliers dibuang
print('Shape awal: ', dataku.shape)

# Removing outliers
retail_raw = dataku[~((dataku['item_price'] < (Q1 - 1.5 * IQR)) | (dataku['item_price'] > (Q3 + 1.5 * IQR)))]

# Check ukuran (baris dan kolom) setelah data yang outliers dibuang
print('Shape akhir: ', retail_raw.shape)