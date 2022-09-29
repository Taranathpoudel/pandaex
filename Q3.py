# 3. Write a Pandas program to add, subtract, multiple and divide two Pandas Series. Go to the editor
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
import pandas as pd
ds1=pd.Series([2,4,6,8,10])
ds2=pd.Series([1,3,5,7,9])

# Convertinng panda series into normal arrays
j=1
i=1
k=1
arr1=[]
arr2=[]
arr3=[]

while(i<=len(ds1)):
    a=ds1[i-1]
    arr1.append(a)
    i=i+1

while(j<=len(ds1)):
    a=ds2[j-1]
    arr2.append(a)
    j=j+1

# Adding two arrays
while(k<=len(ds1) or k<=len(ds2)):
    arr4=arr1[k-1]+arr2[k-1]
    arr3.append(arr4)
    k=k+1

# Converting into panda series
ds3=pd.Series(arr3)
print(ds3)