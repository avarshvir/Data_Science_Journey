import pandas as pd
data =pd.read_csv('datasets/simple_da.csv')
print(data)

#df1 = pd.read_csv('simple_dataset.csv')
data2 = pd.read_csv('datasets/simpple_da2.csv')

# Merge the datasets
data3 = data.merge(data2,how="left")
print(data3)