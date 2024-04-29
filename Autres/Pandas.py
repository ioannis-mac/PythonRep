import pandas as pd

s = pd.Series([10,20,30,40], index=['a','b','c','d'])

print(s)
print(s.values)
print(s.index)
#print(s[0])
print(s.iloc[0])
print(s["a"])

data = pd.Series([0.1,0.4,0.78,0.5], index=['a','b','c','d'])
print(data)
print(data["b"])
data['e'] = 0.9
print(data)