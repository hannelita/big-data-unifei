import scipy.io as sio
import numpy as np
import pandas as pd

path = "C:\Users\Lenio\Dropbox\Doutorado\CERIn Data\CERInData\Data_2018_January-01_to_December-31_30-Seconds"
files = ["CERIn-Big-Data-2018-01-01-to-2018-07-01-Values.xlsx", "CERIn-Big-Data-2018-07-01-to-2019-01-01-Values.xlsx"]

all_data = pd.DataFrame()

for file in files
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)

all_data.describe()
all_data.head()