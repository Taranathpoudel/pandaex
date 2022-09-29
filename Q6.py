'''
6. Write a Pandas program to convert a NumPy array to a Pandas series. Go to the editor
Sample Series:
NumPy array:
[10 20 30 40 50]
Converted Pandas series:
0 10
1 20
2 30
3 40
4 50
dtype: int64
'''
import numpy as  np
narr=np.array([10,20,30,40,50])

# Converting array into ds series
import pandas as pd
ds=pd.Series(narr)
print(ds)