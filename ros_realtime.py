import rospy
from sensor_msgs.msg import PointCloud2, PointField
import sensor_msgs.point_cloud2 as pc2
from roslib import message
import pcl
from show import *
from rospy.numpy_msg import numpy_msg
import cv2

HRES = 0.35         # horizontal resolution (assuming 20Hz setting)
VRES = 1.33          # vertical res
VFOV = (-30.67, 10.67) # Field of view (-ve, +ve) along vertical axis
Y_FUDGE = 5         # y fudge factor for velodyne HDL 64E
im=0
def on_new_point_cloud(data):
	global im
	pc = pc2.read_points(data, skip_nans=True, field_names=("x", "y", "z","intensity"))
	#print pc.type
	#print data.type
	cloud_points = []
	for p in pc:
		cloud_points.append(p)
	npc = np.array(cloud_points)
	#lidar_to_2d_front_view(npc, v_res=VRES, h_res=HRES, v_fov=VFOV, val="depth", y_fudge=Y_FUDGE)
	#lidar_to_2d_front_view(npc, v_res=VRES, h_res=HRES, v_fov=VFOV, val="height", y_fudge=Y_FUDGE)
	#lidar_to_2d_front_view(npc, v_res=VRES, h_res=HRES, v_fov=VFOV, val="reflectance", y_fudge=Y_FUDGE)
	#im = birds_eye_point_cloud(npc, side_range=(-10, 10), fwd_range=(-10, 10), res=0.1)

	im = point_cloud_to_panorama(npc,
                             v_res=VRES,
                             h_res=HRES,
                             v_fov=VFOV,
                             y_fudge=5,
                             d_range=(0,100))

	#plt.imshow(im,cmap='spectral')
	#plt.show()

rospy.init_node('listner',anonymous=True)
rospy.Subscriber('/velodyne_points',numpy_msg(PointCloud2),on_new_point_cloud)
while 1:
	cv2.imshow('image',im)
	cv2.waitKey(1)
cv2.destroyAllWindows()

rospy.spin()


