import pandas as pd
df = pd.read_csv("employees.csv")
dummies = pd.get_dummies(df.EMPLOYEE_ID)
merged = pd.concat([df,dummies], axis ='columns')
merged = merged.drop(['EMPLOYEE_ID','LAST_NAME','EMAIL','PHONE_NUMBER','HIRE_DATE'], axis='columns')
print(merged.to_string())
