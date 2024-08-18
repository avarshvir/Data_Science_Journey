import pandas as pd
data = [1,2,3,4]
print(data)
ps = pd.Series(data)
print(ps)

calories = {"day1": 421, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

#index
print("index...")
ind = pd.Series(data,index = ['x','y','a',1])
print(ind)