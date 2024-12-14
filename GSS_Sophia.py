import pandas as pd

# Path to your Excel file
file_path = r'C:\Users\sghal\Downloads\GSS_Inorganic_Chemicals_Data.xlsx'

# Read the Excel file
df = pd.read_excel(file_path)

# Display the contents of the DataFrame
print(df.head(4))
