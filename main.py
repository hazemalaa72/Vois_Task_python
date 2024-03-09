#!/usr/bin/python
import pandas as pd
import statistics
df = pd.read_csv("D:\Employees.csv")
df.drop_duplicates(inplace = True)
print(df)
malecount=0
femalecount=0
sum=0
avg=0
for x in range (7) :
    df["Age"][x] =df["Age"][x].round(0)
    df["Salary(USD)"][x]=df["Salary(USD)"][x]*50
    sum=sum+df["Age"][x]
    avg=sum/7
    if df["Gender"][x]=="M":
        malecount=malecount+1
    else : femalecount=femalecount+1
df = df.rename(columns={"Salary(USD)":"Salary(EGP)"})
df.to_csv('file.csv', index=False)
print(df)
#print Average
print(avg)
#print median value
print(statistics.median(df["Age"]))
#print Ratio between males and female employees
print(malecount/femalecount)







