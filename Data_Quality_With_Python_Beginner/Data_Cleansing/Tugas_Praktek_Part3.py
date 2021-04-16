import pandas as pd
dataku = pd.read_csv('retail_raw_reduced_data_quality.csv')

# Check ukuran (baris dan kolom) sebelum data duplikasi dibuang
print('Shape awal: ', dataku.shape)

# Buang data yang terduplikasi
dataku.drop_duplicates(inplace=True)

# Check ukuran (baris dan kolom) setelah data duplikasi dibuang
print('Shape akhir: ', dataku.shape)