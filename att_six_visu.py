# six forklift CSV visualisation with bokeh

from mpl_toolkits.mplot3d import Axes3D as Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import os
import os.path
import glob
import numpy as np


os.chdir("/home/vassb/fingerprint_data/ansgar_att_six_forklift_att_merged/")
export_location = "/home/vassb/fingerprint_data/ansgar_att_six_forklift_att_merged/"

file_list = glob.glob('*.csv')



for file in file_list:
    temp_df = pd.DataFrame(pd.read_csv(file))
    # NEEDED?
    # temp_df = temp_df[complete.cases(temp_df),]
    temp_df.columns
    
    for wl_wol in [0, 1]:
        for s_type in range(1,max(temp_df["steering_cat"])+1):
            #Dynamic
            plot_df = temp_df[np.logical_and(temp_df.steering_cat == s_type,temp_df['is.weight'] == wl_wol)]
            x = plot_df["Speed_Drivemotor_1_RPM"]
            y = plot_df["Torque_Drivemotor_1_Nm"]
            hist, xedges, yedges = np.histogram2d(x, y, bins=8, range=[
                [-5500, 5500],
                [-80, 80]])

            m = np.asmatrix(np.rot90(hist))
            result = np.zeros((9, 9))
            result[:m.shape[0], :m.shape[1]] = m

            pd.DataFrame(result, index=[str(n) for n in yedges[::-1]], columns=[str(n) for n in xedges]).to_csv(
                export_location +"Dynamic_"+ os.path.splitext(file)[0] +"_s_type:_"+ str(s_type)+ "_wl_wol:_"+ str(wl_wol)+ "_3Dplot.csv")

        #Stress_
        # plot_df = temp_df.query('steering_cat == s_type')
        # x = plot_df["date_time"]
        # y = plot_df["Torque_Drivemotor_1_Nm"]
        # hist, xedges, yedges = np.histogram2d(x, y, bins=8, range=[
        #     [min(temp_df["Speed_Drivemotor_1_RPM"]), max(temp_df["Speed_Drivemotor_1_RPM"])],
        #     [min(temp_df["Torque_Drivemotor_1_Nm"]), max(temp_df["Torque_Drivemotor_1_Nm"])]])
        #
        # m = np.asmatrix(np.rot90(hist))
        # result = np.zeros((9, 9))
        # result[:m.shape[0], :m.shape[1]] = m
        #
        # pd.DataFrame(result, index=[str(n) for n in yedges[::-1]], columns=[str(n) for n in xedges]).to_csv(
        #     export_location + "Stress_" + os.path.splitext(file)[0] + "_wl_wol_" + wl_wol + "_3Dplot.csv")
        # hist3D_fancy(x=as.numeric(
        #     plot_df$date_time), y = plot_df$Torque_Drivemotor_1_Nm, breaks = 8, xlab = "RPM", ylab = "Nm", breaks = 8, main = paste(
        #     "Stress_", gsub(".csv", "", file, fixed=TRUE), "_wl_wol_", wl_wol, "_3Dplot.png", sep=""))
        # png(filename=paste(export_location, "Stress_", gsub(".csv", "", file, fixed=TRUE), "_wl_wol_", wl_wol,
        #                    "_3Dplot.png", sep=""))

        #Travelling_

        # hist3D_fancy(x=as.numeric(
        #     plot_df$date_time), y = plot_df$Speed_Drivemotor_1_RPM, breaks = 8, xlab = "RPM", ylab = "Nm", breaks = 8, main = paste(
        #     "Travelling_", gsub(".csv", "", file, fixed=TRUE), "_wl_wol_", wl_wol, "_3Dplot.png", sep=""))
        # png(filename=paste(export_location, "Travelling_", gsub(".csv", "", file, fixed=TRUE), "_wl_wol_", wl_wol,
        #                    "_3Dplot.png", sep=""))
