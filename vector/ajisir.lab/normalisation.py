import pandas as pd
df=pd.read_csv('PublicSchools.csv')
print(df)
df_normal = df.copy()
for column in df_normal.columns:
     df_normal[column]=(df_normal[column]-df_normal[column].min())/(df_normal[column].max()-df_normal[column].min())
print(df_normal)
