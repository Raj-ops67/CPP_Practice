#Pandas Series and DataFrame
import pandas as pd
marks=pd.Series [85, 91, 78, 88, 95]
index= ["A", "B", "C", "D","E"]
print (" --- Panda Series ---")
print (marks)
data = {
    "RollNo": [101, 102, 103, 104, 105],
    "Name": ["Anitha", "Bala", "Chitra", "Dinesh", "Ezhil"],
    "Department": ["CSE", "CSE", "ECE", "CSE", "ECE"],
    "Marks": [85, 91, 78, 88, 95]
}
df= pd.DataFrame(data)
print("\n ---Data Frame---")
print(df)
print("\nAverage Mark:", round (df["Marks"].means(),2))
print("\n Students scoring above 85:")
print(df[df["Marks"]>85])
