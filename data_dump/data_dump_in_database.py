import pandas as pd
from utils import df_to_db



digital_data = pd.read_csv(r'C:\Users\Lenovo ThinkPad T460\Downloads\employees - Sheet1.csv')
# print(digital_data)
df = pd.DataFrame.from_records(digital_data)
print('\n')
# print(df)
# print(df['name'])
# print(f"{len(df.index)=} Done")

# to generate a csv output file in order to validate the data
# df.to_csv('digital_data.csv', sep=',', index=False)

df_col_str = """name,salary,department,emp_date"""
on_conflict_columns = """"""

output = df_to_db(df, 'public.employees', df_col_str, on_conflict_columns)

