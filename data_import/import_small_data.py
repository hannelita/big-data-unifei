import scipy.io as sio
import numpy as np
import pandas as pd
from os import getcwd
from os.path import join as pjoin
from pathlib import Path
from datetime import datetime, date, time

def convert_mat_file_to_pandas():
    mat_contents = sio.loadmat("D:\Develop\BigData\LocalFiles\Importer\data\Inv1x160x161x0.mat")
    mat_values = {key:value for key, value in mat_contents.items() if key[0] != '_' }
    return pd.DataFrame({key:pd.Series(value[0]) for key, value in mat_values.items()})

pandas = convert_mat_file_to_pandas()
#print(pandas)

for col in list(pandas):
    #print("New Line", pandas[col])
    #pandas[pandas[col] < np.percentile(pandas[col],95)]
    arr_col = (pandas[col] < np.percentile(pandas[col],99))
    print("Coluna: ", col, " Percentile: ", np.percentile(pandas[col],95), 
          " Size: ", len(arr_col))

print(pandas)
print(pandas)