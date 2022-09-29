# 2. Write a Pandas program to convert a Panda module Series to Python list and it's type
import pandas as pd
import numpy as np
ds=pd.Series([1,2,3,4,5,6,7,8,9])
arr=[]
j=1
while(j<=len(ds)):
    arr1=ds[j-1]
    arr.append(arr1)
    j=j+1

print(arr)