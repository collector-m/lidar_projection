import pcl
import numpy as np


def load_pc_from_pcd(pcd_path):
    """Load PointCloud data from pcd file."""
    p = pcl.load(pcd_path)
    return np.array(list(p), dtype=np.float32)

def load_pc_from_bin(bin_path):
    """Load PointCloud data from pcd file."""
    obj = np.fromfile(bin_path, dtype=np.float32).reshape(-1, 4)
    return obj
