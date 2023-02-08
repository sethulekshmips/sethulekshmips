import pandas as pd
import math
df=pd.read_csv('employeenumber .csv')
print(df)
def get_mean(array):
    sum=0
    for i in array:
        sum=sum+i
        mean=sum/len(array)
    return mean

def get_std(array):
    mean=get_mean(array)
    sumdiff=0
    for i in array:
        sumdiff = sumdiff+ (i-mean)**2
        varience = sumdiff/(len(array)-1)
        stddev = math.sqrt(varience)
    return stddev

for i in df.columns:
    print(get_std(df[i]))
