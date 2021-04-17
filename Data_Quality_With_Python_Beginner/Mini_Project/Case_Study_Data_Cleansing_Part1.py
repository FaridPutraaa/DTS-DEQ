import pandas as pd
import matplotlib.pyplot as plt
uncleaned_raw = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/uncleaned_raw.csv')
#Mengetahui kolom yang memiliki outliers!
uncleaned_raw.boxplot()
plt.show()