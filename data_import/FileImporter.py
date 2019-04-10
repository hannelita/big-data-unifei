import scipy.io as sio
import numpy as np
import pandas as pd
from os import getcwd
from os.path import join as pjoin
from pathlib import Path
from datetime import datetime, date, time

def getfullfilesnames():
    fullfilenames = []
    for file in list(Path(".").rglob("*.[mM][aA][tT]")):
        fullfilenames.insert(0,pjoin(getcwd(), file))
    return fullfilenames;

def readmatfiles(files):
    mat_contents = sio.loadmat(files[0])
    mat_values = {key:value for key, value in mat_contents.items() if key[0] != '_' }
    data = pd.DataFrame({key:pd.Series(value[0]) for key, value in mat_values.items()})
    print(data)

files = getfullfilesnames();
readmatfiles(files)