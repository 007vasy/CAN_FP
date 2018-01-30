# 700 MB *.mat files observation reduce from 0.01s to 1s with mean and save as *.csv
import scipy.io
import pandas as pd
import os
import glob

os.chdir("/home/vassb/fingerprint_data/")
export_location="/home/vassb/fingerprint_data/ansgar_att_six_forklift/"

wd_filenames = glob.glob('*.mat')

#for file in wd_filenames:
#   temp_dict=scipy.io.loadmat(file)
#   for name,dict_ in temp_dict.items():
#       print name

temp_dict=scipy.io.loadmat('Part 01 Daimler F 00150 MultiTimeChannel.mat')
for name,dict_ in temp_dict.items():
    print name
    #temp_df.head()
    #print dict_
    temp_df = pd.DataFrame(temp_dict[[name]])
    temp_df.head()
