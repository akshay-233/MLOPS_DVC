import pandas as pd 
import os

data={'Name':["Alice","Bob","charlie"],
      'Age':[40,38,40],
      'City':["San Fransico","CHicago","Texas"]
        }

df=pd.DataFrame(data)

#"Ensure the data directory exists over root level"
data_dir='data'
os.makedirs(data_dir,exist_ok=True)

#Define the file path
file_path=os.path.join(data_dir,'Sample_data.csv')

# save the dataframe to csv including column names
df.to_csv(file_path,index=False)
