import pandas as dp
data={'rollno':[1,2,3,4,5,],
      'name':["anu","manu","paru","vinu","ramu"],
      'physics':[34,67,89,90,65],
      'maths':[56,78,90,45,65,],
      'biology':[56,89,99,88,87],
      'chemistry':[67,89,90,56,98],
      'english':[76,89,56,47,93]}
df=dp.DataFrame(data)
print(df)
print("_________________________________")
df=df.eval('total=physics+maths+biology+chemistry+english')
print(df)
print("____________________________________")
max_mark = df['total'].max()
max_physics=df['physics'].max()
max_mat=df['maths'].max()
max_bio=df['biology'].max()
max_chem=df['chemistry'].max()
max_eng=df['english'].max()
print("the highest total:",max_mark)
print("highest score in physics:",max_physics)
print("highestscore in maths",max_mat)
print("highestscore in biology:",max_bio)
print("highestscore in chemistry:",max_chem)
print("highestscore in english:",max_eng)
print(df.loc[df['total']==max_mark])
print(df.loc[df['biology']==max_bio])