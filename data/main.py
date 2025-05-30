import pandas as pd
import os

data_folder = 'data'
csv_files=[f for f in os.listdir(data_folder) if f.endswith('.csv')]
all_data =[]
for file in csv_files:
  df = pd.read_csv(os.path.join(data_folder,file)) 
  df = df[df["product"]=="pink morsel"] 
  df["sales"] =df["quantity"]*df["price"]
  df = df[["sales","date","region"]]
  all_data.append(df)
final_df =pd.concat(all_data,ignore_index=True)
final_df.to_csv("formatted_sales_data.csv", index=False)
print(" Done! Output saved in 'formatted_sales_data.csv'")

 