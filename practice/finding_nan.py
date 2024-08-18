import numpy as np
import pandas as pd
df = pd.read_csv("property_data.csv")
data = df.head()
print(data)

#finding NAN values and NAN type-values

print((df['No_Books']))
print(df['No_Books'].isnull())

count = 0
for item in df['property_data.csv']:
    try:
        int(item)
        df.loc[count, ] = np.nan
    except ValueError:
        count+=1

print(df.isnull().sum())