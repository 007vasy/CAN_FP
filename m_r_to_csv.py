# 700 MB *.mat files observation reduce from 0.01s to 1s with mean and save as *.csv
import scipy.io
import pandas as pd
import os
import os.path
import glob
import numpy as np

os.chdir("/home/vassb/fingerprint_data/")
export_location="/home/vassb/fingerprint_data/ansgar_att_six_forklift/"

wd_filenames = glob.glob('*.mat')

for file in wd_filenames:
    print file
    output_df = pd.DataFrame()
    flag = True
    temp_dict=scipy.io.loadmat(file)
    for name,dict_ in temp_dict.items():
        #print name
        #temp_df.head()
        #print dict_
        temp_df = pd.DataFrame(dict_, columns=['time_ID_s',str(name)])
        del temp_dict[name]
        temp_df[['time_ID_s']] = temp_df[['time_ID_s']].apply(np.floor)
        temp_df = temp_df.groupby(by='time_ID_s', as_index=False)[[name]].mean()
        # print temp_df.head()
        # print temp_df.tail()
        if(flag):
            output_df = temp_df
            flag = False
        else:
            output_df = output_df.merge(temp_df, how='outer', on = 'time_ID_s')
        # print output_df.columns
    filename, file_extesions = os.path.splitext(file)
    output_df.to_csv(export_location +'_'+ filename +'.csv',index=False)
    print file + ' converted and reduced to ' + filename +'.csv'