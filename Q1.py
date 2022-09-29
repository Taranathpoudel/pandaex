# 1. Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using Pandas module.
import pandas as pd
i=int(input("Enter number of elements: "))
j=1
arr=[]
while (j<=i):
    a=int(input('Enter elements: '))
    arr.append(a)
    j=j+1

ds=pd.Series(arr)
print(ds)