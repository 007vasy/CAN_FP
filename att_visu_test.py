# six forklift CSV visualisation with bokeh

from mpl_toolkits.mplot3d import Axes3D as Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import os
import os.path
import glob
import numpy as np



#os.chdir("/home/vassb/fingerprint_data/ansgar_att_six_forklift_att_merged/")
#export_location = "/home/vassb/fingerprint_data/ansgar_att_six_forklift_att_merged/"


temp_df = pd.DataFrame(pd.read_csv("/media/vasy/Data/Doksik/projekts/AITIA/can_fp_att_merged/IMRl_F_00214_att_merged.csv"))
temp_df = temp_df.dropna(how='any')


fig = plt.figure()
ax = Axes3D(fig)

x = temp_df["Speed_Drivemotor_1_RPM"]
y = temp_df["Torque_Drivemotor_1_Nm"]
hist, xedges, yedges = np.histogram2d(x, y, bins=8, range=[[min(temp_df["Speed_Drivemotor_1_RPM"]), max(temp_df["Speed_Drivemotor_1_RPM"])], [min(temp_df["Torque_Drivemotor_1_Nm"]), max(temp_df["Torque_Drivemotor_1_Nm"])]])



# Note: np.meshgrid gives arrays in (ny, nx) so we use 'F' to flatten xpos,
# ypos in column-major order. For numpy >= 1.7, we could instead call meshgrid
# with indexing='ij'.
xpos, ypos = np.meshgrid(xedges[:-1], yedges[:-1])
xpos = xpos.flatten('F')
ypos = ypos.flatten('F')
zpos = np.zeros_like(xpos)

# Construct arrays with the dimensions for the 16 bars.
dx = 5 * np.ones_like(xpos)
#dy = dx.copy()
dy = 5 * np.ones_like(ypos)
dz = hist.flatten()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='g', zsort='average')

plt.show()

m= np.asmatrix(np.rot90(hist))
result = np.zeros((9,9))
result[:m.shape[0],:m.shape[1]] = m

pd.DataFrame(result,index=[str(n) for n in yedges[::-1]],columns=[str(n) for n in xedges]).to_csv("foo6.csv")

result = np.zeros((9,9))
m = np.asmatrix([[1 , 2],[3,4]])

result[:m.shape[0],:m.shape[1]] = m

temp_df = pd.DataFrame(pd.read_csv("/media/vasy/Data/Doksik/projekts/AITIA/reduced_can_fp/merged_machines/IMRl_F_00214_att_merged.csv"))
    # NEEDED?
temp_df = temp_df.dropna(how='any')
temp_df["is.weight"].astype(str).astype(bool)
temp_df["steering_cat"] = temp_df["steering_cat"].astype(str)

export_location = "/media/vasy/Data/Doksik/projekts/AITIA/reduced_can_fp/merged_machines/"

for wl_wol in [0, 1]:
    for s_type in range(1,max(temp_df["steering_cat"])):
        #Dynamic
        plot_df = temp_df.query('steering_cat == ' + int(s_type) + "and 'is.weight' == " + wl_wol)
        x = plot_df["Speed_Drivemotor_1_RPM"]
        y = plot_df["Torque_Drivemotor_1_Nm"]
        hist, xedges, yedges = np.histogram2d(x, y, bins=8, range=[
            [min(temp_df["Speed_Drivemotor_1_RPM"]), max(temp_df["Speed_Drivemotor_1_RPM"])],
            [min(temp_df["Torque_Drivemotor_1_Nm"]), max(temp_df["Torque_Drivemotor_1_Nm"])]])

        m = np.asmatrix(np.rot90(hist))
        result = np.zeros((9, 9))
        result[:m.shape[0], :m.shape[1]] = m

        pd.DataFrame(result, index=[str(n) for n in yedges[::-1]], columns=[str(n) for n in xedges]).to_csv(export_location +"Dynamic_"+ os.path.splitext(file)[0] +"_s_type:"+ s_type+ "_wl_wol_"+ wl_wol+ "_3Dplot.csv")

      temp_df.dtypes
