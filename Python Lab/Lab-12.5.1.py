#Lab 12.5.1
import pandas as nils
filename="D:/5th semester/Python/XLSS_CSV/FSINULL.xlsx"
df=nils.read_excel(filename)
print(df.isnull())
totalnull=df.isnull().sum()
print("Total number of null values",totalnull)