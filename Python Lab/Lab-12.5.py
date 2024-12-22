#Creating Dataframes from CSV file
import pandas as nn
name="D:/5th semester/Python/XLSS_CSV/output.csv"
df=nn.read_csv(name,on_bad_lines="skip")
print()
print("Display the dimensions of the dataframe",df.ndim)
print()
print(" check if the dataframe is empty:\n",df.empty)
print()
print("Display the Transpose of the dataframe:\n",df.T)

