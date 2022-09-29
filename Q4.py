# 4. Write a Pandas program to compare the elements of the two Pandas Series. Go to the editor
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]
from symbol import comparison
import pandas as pd
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
i = 1
print(ds1)
print('\n')
print(ds2)
# comparison
while(i <= len(ds1)):
    if (ds1[i-1] > ds2[i-1]):
        print(ds1[i-1], "is greather than", ds2[i-1])
    elif (ds1[i-1] < ds2[i-1]):
        print(ds1[i-1], "is less than", ds2[i-1])
    else:
        print(ds1[i-1], "is equal", ds2[i-1])
    i = i+1
