
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import os.path
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/media/vasy/Data/Doksik/projekts/AITIA/reduced_can_fp/merged_machines")
export_location = "/media/vasy/Data/Doksik/projekts/AITIA/reduced_can_fp/histogramm3d_data"

temp_df = pd.DataFrame(pd.read_csv("/media/vasy/Data/Doksik/projekts/AITIA/can_fp_att_merged/IMRl_F_00214_att_merged.csv"))
plot_df = temp_df.dropna(how='any')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = plot_df["Speed_Drivemotor_1_RPM"]
y = plot_df["Torque_Drivemotor_1_Nm"]
hist, xedges, yedges = np.histogram2d(x, y, bins=8, range=[
                [-5500, 5500],
                [-80, 80]])

# Construct arrays for the anchor positions of the 16 bars.
# Note: np.meshgrid gives arrays in (ny, nx) so we use 'F' to flatten xpos,
# ypos in column-major order. For numpy >= 1.7, we could instead call meshgrid
# with indexing='ij'.
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25)
xpos = xpos.flatten('F')
ypos = ypos.flatten('F')
zpos = np.zeros_like(xpos)

# Construct arrays with the dimensions for the 16 bars.
dx = 1000 * np.ones_like(xpos)
dy = 15 * np.ones_like(ypos)
dz = hist.flatten()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='g', zsort='average',alpha=0.5)
ax.set_xlabel('Speed_Drivemotor_1_RPM')
ax.set_ylabel('Torque_Drivemotor_1_Nm')
ax.set_zlabel('Occurrence')

plt.show()
