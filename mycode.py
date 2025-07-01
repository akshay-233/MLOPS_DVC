import pandas as pd 
import os

data={'Name':["Alice","Bob","charlie"],
      'Age':[40,38,40],
      'City':["San Fransico","CHicago","Texas"]
        }

df=pd.DataFrame(data)

#Adding new row to df v2
new_row1={'Name':"F1",'Age':38,'City':"San Fransico"}
df.loc[len(df.index)]=new_row1

#Adding new row to df v3
new_row2={'Name':"F2",'Age':37,'City':"Wellington"}
df.loc[len(df.index)]=new_row2

#"Ensure the data directory exists over root level"
data_dir='data'
os.makedirs(data_dir,exist_ok=True)

#Define the file path
file_path=os.path.join(data_dir,'Sample_data.csv')

# save the dataframe to csv including column names
df.to_csv(file_path,index=False)
