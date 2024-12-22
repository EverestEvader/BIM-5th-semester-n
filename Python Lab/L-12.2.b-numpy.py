import pandas as pd
# Simple list
data = [["Ram", 101], ["Hari",105], ["Sita",108]]
# Convert to DataFrame
df = pd.DataFrame(data, columns=['Name','ID'])
print(df)