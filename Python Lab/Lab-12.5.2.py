import pandas as pd
filename = "D:/5th semester/Python/XLSS_CSV/FSINULL.xlsx"
df = pd.read_excel(filename)
print(df[df.isna().any(axis =1)])
#Filling the missing values with the mean valuesdf 
df['Demo'].fillna(df['Demo'].mean(), inplace = True)
df['Refugees'].fillna(df['Refugees'].mean(), inplace = True)
df['Group'].fillna(df['Group'].mean(), inplace = True)
df['Flight'].fillna(df['Flight'].mean(), inplace = True)
df['Country'].fillna('No_Country', inplace = True)
print()
col1 = df['Country']
print(col1) 
col2 = df[['Group','Flight']]
print(col2)
