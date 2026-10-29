import pandas as pd
import numpy as np 
data = {
"ID":[101,102,103,104,105,105],
"age":[20,22,250,np.nan,21,21],
"city":["mosul","erbil","mosul","basra","mosul","mosul"],
"GPA":[3.2,3.5,3.0,3.8,3.4,3.4]
}
df = pd.DataFrame(data)
print("original dataset:")
print(df)
df = df.drop_duplicates()
df.loc[df["age"]==250,"age"]=25
mean_age = df["age"].mean()
df["age"]=df["age"].fillna(mean_age)
average_gpa = df["GPA"].mean()
print("\n cleaned database:")
print (df)
print("\n average GPA",round(average_age,2))