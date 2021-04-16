import pandas as pd
dataku = pd.read_csv('retail_raw_reduced_data_quality.csv')

print('Descriptive Statistic Part 1')
print('============================')
# Kolom city
length_city = len(dataku['city'])
print('Length kolom city:', length_city)

# Tugas Praktek: Kolom product_id
length_product_id = len(dataku['product_id'])
print('Length kolom product_id:', length_product_id)
print('============================')
print('\n')

print('Descriptive Statistic Part 2')
print('============================')
# Count kolom city
count_city = dataku['city'].count()
print('Count kolom city:', count_city)

# Tugas praktek: count kolom product_id
count_product_id = dataku['product_id'].count()
print('Count kolom product_id:', count_product_id)
print('============================')
print('\n')

print('Descriptive Statistic Part 3')
print('============================')
# Missing value pada kolom city
number_of_missing_values_city = length_city - count_city
float_of_missing_values_city = float(number_of_missing_values_city/length_city)
pct_of_missing_values_city = '{0:.1f}%'.format(float_of_missing_values_city * 100)
print('Persentase missing value kolom city:', pct_of_missing_values_city)

# Tugas praktek: Missing value pada kolom product_id
number_of_missing_values_product_id = length_product_id - count_product_id
float_of_missing_values_product_id = float(number_of_missing_values_product_id/length_product_id)
pct_of_missing_values_product_id = '{0:.1f}%'.format(float_of_missing_values_product_id * 100)
print('Persentase missing value kolom product_id:', pct_of_missing_values_product_id)
print('============================')
print('\n')

print('Descriptive Statistic Part 4')
print('============================')
# Deskriptif statistics kolom quantity
print('Kolom quantity')
print('Minimum value: ', dataku['quantity'].min())
print('Maximum value: ', dataku['quantity'].max())
print('Mean value: ', dataku['quantity'].mean())
print('Mode value: ', dataku['quantity'].mode())
print('Median value: ', dataku['quantity'].median())
print('Standard Deviation value: ', dataku['quantity'].std())

# Tugas praktek: Deskriptif statistics kolom item_price
print('')
print('Kolom item_price')
print('Minimum value: ', dataku['item_price'].min())
print('Maximum value: ', dataku['item_price'].max())
print('Mean value: ', dataku['item_price'].mean())
print('Median value: ', dataku['item_price'].median())
print('Standard Deviation value: ', dataku['item_price'].std())
print('============================')
print('\n')

print('Descriptive Statistic Part 5')
print('============================')
# Quantile statistics kolom quantity
print('Kolom quantity:')
print(dataku['quantity'].quantile([0.25, 0.5, 0.75]))

# Tugas praktek: Quantile statistics kolom item_price
print('')
print('Kolom item_price:')
print(dataku['item_price'].quantile([0.25, 0.5, 0.75]))
print('============================')
print('\n')


print('Descriptive Statistic Part 5')
print('============================')
print('Korelasi quantity dengan item_price')
print(dataku[['quantity', 'item_price']].corr())
print('============================')
print('\n')