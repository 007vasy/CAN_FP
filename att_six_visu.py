# six forklift CSV visualisation with bokeh

from mpl_toolkits.mplot3d import Axes3D as Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import os
import os.path
import glob
import numpy as np

def Steering_Cat(x):
    if abs(x) <= 30:
        return 1
    elif abs(x) <= 60:
        return 2
    else:
        return 3

os.chdir("/home/vassb/fingerprint_data/ansgar_att_six_forklift_att_merged/")
export_location = "/home/vassb/fingerprint_data/ansgar_att_six_forklift_att_merged/"

file_list = glob.glob('*.csv')

for file in file_list:
    temp_df = pd.DataFrame(pd.read_csv(file))
    # NEEDED?
    # temp_df = temp_df[complete.cases(temp_df),]
    temp_df[["steering_cat"]] = Steering_Cat(temp_df[["Steering_angle_angle"]])

    for wl_wol in [0, 1]:
        for s_type in range(1,max(temp_df["steering_cat"])):
            plot_df = temp_df.query('steering_cat == s_type and is.weight == wl_wol')

            # hist3D_fancy(
            #     x=plot_df$Speed_Drivemotor_1_RPM, y = plot_df$Torque_Drivemotor_1_Nm, xlab = "RPM", ylab = "Nm", breaks = 8, main = paste(
            #     "Dynamic_", gsub(".csv", "", file, fixed=TRUE), "_s_type:", s_type, "_wl_wol_", wl_wol, "_3Dplot.png", sep=""))
            # png(filename=paste(export_location, "Dynamic_", gsub(".csv", "", file, fixed=TRUE), "_s_type:", s_type, "_wl_wol_",
            #                    wl_wol, "_3Dplot.png", sep=""))
            # }
        plot_df = temp_df.query('steering_cat == s_type')
        # hist3D_fancy(x=as.numeric(
        #     plot_df$date_time), y = plot_df$Torque_Drivemotor_1_Nm, breaks = 8, xlab = "RPM", ylab = "Nm", breaks = 8, main = paste(
        #     "Stress_", gsub(".csv", "", file, fixed=TRUE), "_wl_wol_", wl_wol, "_3Dplot.png", sep=""))
        # png(filename=paste(export_location, "Stress_", gsub(".csv", "", file, fixed=TRUE), "_wl_wol_", wl_wol,
        #                    "_3Dplot.png", sep=""))

        # hist3D_fancy(x=as.numeric(
        #     plot_df$date_time), y = plot_df$Speed_Drivemotor_1_RPM, breaks = 8, xlab = "RPM", ylab = "Nm", breaks = 8, main = paste(
        #     "Travelling_", gsub(".csv", "", file, fixed=TRUE), "_wl_wol_", wl_wol, "_3Dplot.png", sep=""))
        # png(filename=paste(export_location, "Travelling_", gsub(".csv", "", file, fixed=TRUE), "_wl_wol_", wl_wol,
        #                    "_3Dplot.png", sep=""))

fig = plt.figure()
ax = Axes3D(fig)
x, y = np.random.rand(2, 100) * 4
hist, xedges, yedges = np.histogram2d(x, y, bins=4, range=[[0, 4], [0, 4]])

# Construct arrays for the anchor positions of the 16 bars.
# Note: np.meshgrid gives arrays in (ny, nx) so we use 'F' to flatten xpos,
# ypos in column-major order. For numpy >= 1.7, we could instead call meshgrid
# with indexing='ij'.
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25)
xpos = xpos.flatten('F')
ypos = ypos.flatten('F')
zpos = np.zeros_like(xpos)

# Construct arrays with the dimensions for the 16 bars.
dx = 0.5 * np.ones_like(zpos)
dy = dx.copy()
dz = hist.flatten()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='g', zsort='average')

plt.show()