import scipy.io as sio
import numpy as np
import pandas as pd

file_path = "E:\\Cerin_big-data\\"
#data = spark.read.csv(file_path + "*.csv", header=True)
data = spark.read.option("delimiter", ";").option("header", "true").csv(file_path + "*.csv")


def import_file():       

    #sc.
    all_data = pd.DataFrame()

    path = "E:\\Cerin_big-data\\"
    files = ["Test-Jan-01-Jan-05.csv", "Test-Jul-01-Jul-05.csv"]
    #files = ["Test-InvalidValues.xlsx"]

    for f in files:
        full_path = path + f
        print(full_path)
        df = pd.read_excel(full_path)
        all_data = all_data.append(df,ignore_index=True)

    return all_data

def show_info(column, percentil, last_size , current_size):
    print("Column: {:>7} \t Percentile: {:>18} \t Before/Current/Removed: {:>8} / {:>8} / {:>5}"
        .format(column, percentil, last_size, current_size, last_size - current_size))
		
def filter_data(dataset):
    last_size = len(dataset)
    for column in list(dataset):
        dataset = dataset[pd.to_numeric(dataset[column], errors='coerce').notnull()]
        percentil = np.percentile(dataset[column],1, interpolation='lower')
        dataset = dataset[dataset[column] > percentil]
        
        current_size = len(dataset[column])
        show_info(column, percentil, last_size, current_size)        
        last_size = current_size
    return dataset	

#if __name__ == '__main__':
    #data = import_file()
    #data.describe()