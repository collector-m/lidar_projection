import matplotlib.pyplot as plt
import numpy as np
import pcl
from show import *
from tool import *

points=load_pc_from_bin('bin/83.bin')
lidar = points

HRES = 0.35         # horizontal resolution (assuming 20Hz setting)
VRES = 0.4          # vertical res
VFOV = (-24.9, 2.0) # Field of view (-ve, +ve) along vertical axis
Y_FUDGE = 5         # y fudge factor for velodyne HDL 64E

lidar_to_2d_front_view(lidar, v_res=VRES, h_res=HRES, v_fov=VFOV, val="depth",
                       saveto="pic/lidar_depth.png", y_fudge=Y_FUDGE)

lidar_to_2d_front_view(lidar, v_res=VRES, h_res=HRES, v_fov=VFOV, val="height",
                       saveto="pic/lidar_height.png", y_fudge=Y_FUDGE)

lidar_to_2d_front_view(lidar, v_res=VRES, h_res=HRES, v_fov=VFOV,
                       val="reflectance", saveto="pic/lidar_reflectance.png",
                       y_fudge=Y_FUDGE)

birds_eye_point_cloud(lidar, side_range=(-10, 10), fwd_range=(-10, 10), res=0.1, saveto="pic/lidar_pil_01.png")

im = point_cloud_to_panorama(points,
                             v_res=0.42,
                             h_res=0.35,
                             v_fov=(-24.9, 2.0),
                             y_fudge=3,
                             d_range=(0,100))
plt.imshow(im,cmap='spectral')
plt.savefig("pic/spec.png")
#plt.show()

