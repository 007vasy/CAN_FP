# six forklift CSV visualisation with bokeh

from mpl_toolkits.mplot3d import Axes3D as Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import os
import os.path
import glob
import numpy as np

def Steering_Cat(x):
    if (abs(x) <= 30).bool():
        return 1
    elif (abs(x) <= 60).bool():
        return 2
    else:
        return 3

#os.chdir("/home/vassb/fingerprint_data/ansgar_att_six_forklift_att_merged/")
#export_location = "/home/vassb/fingerprint_data/ansgar_att_six_forklift_att_merged/"


temp_df = pd.DataFrame(pd.read_csv("/media/vasy/Data/Doksik/projekts/AITIA/can_fp_att_merged/IMRl_F_00214_att_merged.csv"))
# NEEDED?
temp_df = temp_df.dropna(how='any')
temp_df[["steering_cat"]] = temp_df[["Steering_angle_angle"]].apply(np.vectorize(Steering_Cat))


fig = plt.figure()
ax = Axes3D(fig)
x = temp_df["Speed_Drivemotor_1_RPM"]
y = temp_df["Torque_Drivemotor_1_Nm"]
hist, xedges, yedges = np.histogram2d(x, y, bins=8, range=[[min(temp_df[["Speed_Drivemotor_1_RPM"]]), max(temp_df[["Speed_Drivemotor_1_RPM"]])], [temp_df[["Torque_Drivemotor_1_Nm"]], temp_df[["Torque_Drivemotor_1_Nm"]]]])

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