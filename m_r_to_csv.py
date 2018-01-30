# 700 MB *.mat files observation reduce from 0.01s to 1s with mean and save as *.csv
import scipy
import pandas as pd
import os
import glob

os.chdir("/home/vassb/fingerprint_data/")
export_location="/home/vassb/fingerprint_data/ansgar_att_six_forklift/"

wd_filenames = glob.glob('*.mat')

for file in wd_filenames:
    temp_list=scipy.io.loadmat(file)
    print temp_list.colums    