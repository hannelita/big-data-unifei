import scipy.io as sio
import numpy as np
import pandas as pd

def convert_mat_file_to_pandas():
    mat_contents = sio.loadmat("D:\Develop\BigData\LocalFiles\Importer\data\Inv1x160x161x0.mat")
    mat_values = {key:value for key, value in mat_contents.items() if key[0] != '_' }
    return pd.DataFrame({key:pd.Series(value[0]) for key, value in mat_values.items()})

def remove_columns(dataset):
    return dataset.drop('fS', axis=1)
	
def show_info(column, percentil, last_size , current_size):
    print("Column: {:>7} \t Percentile: {:>18} \t Before/Current/Removed: {:>8} / {:>8} / {:>5}"
        .format(column, percentil, last_size, current_size, last_size - current_size))

def filter_data(dataset):
    last_size = len(dataset)
    for column in list(dataset):        
        percentil = np.percentile(dataset[column],1, interpolation='lower')
        dataset = dataset[dataset[column] > percentil]
        
        current_size = len(dataset[column])
        show_info(column, percentil, last_size, current_size)        
        last_size = current_size
    return filtered

pandas = convert_mat_file_to_pandas()
pandas = remove_columns(pandas)
display(filter_data(pandas))	