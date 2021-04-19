import pandas as pd
import numpy as np

array_df = np.array([[1,2,3,5],
                    [5,6,7,8],
                    ['a', 'b', 9, 10]])
df = pd.DataFrame(array_df)

print(df.iloc[2,0:2] = [11,12])