# 5. Write a Pandas program to convert a dictionary to a Pandas series. Go to the editor
# Sample Series:
# Original dictionary:
# {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
# Converted series:
# a 100
# b 200
# c 300
# d 400
# e 800
import pandas as pd
dict={
    'a':100,
    'b':200,
    'c':300,
    'd':400,
    'e':800
}
# Creating an array
arr=[]
for x in dict.values():
    arr.append(x)

# Converting array into panda series
ds=pd.Series(arr)
print(ds)