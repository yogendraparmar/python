import pandas as pd
data = {"Name":['Yogendra','Raju','Jitu','Mahesh','Rahesj','Raghvendra','Ramu','Nitesh','Shruti','Deepa'],
        "Age":[42,32,23,34,38,31,23,45,24,43],
        "Salary":[20000,23000,22000,23500,25000,43000,45999,24000,18000,54000]}
df = pd.DataFrame(data)
print(df.head(6))
print(df.info())
print(df.tail())
print(df.shape)
#df.to_csv("outpua.csv", index=False)
print(df.describe())

print("datta filter by onmy singa")
samp= df[["Name","Salary"]] #this is use for filter by column
print(samp) 



