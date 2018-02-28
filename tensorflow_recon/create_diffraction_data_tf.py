import xdesign
from xdesign.propagation import *
from xdesign.plot import *
from xdesign.acquisition import Simulator
import h5py
from scipy.ndimage.interpolation import rotate
import numpy as np
import tensorflow as tf
from tensorflow.contrib.image import rotate as tf_rotate

from util import *


# ============================================
# DO NOT ROTATE PROGRESSIVELY
# (DO NOT CONTINUE TO ROTATE AN INTERPOLATED OBJECT)
# ============================================

PI = 3.1415927

# ============================================
theta_st = 0
theta_end = 2 * PI
n_theta = 500
img_dim = 64
energy_ev = 5000
psize_cm = 1e-7
# ============================================

def rotate_and_project(i, obj):

    # coord_old = read_origin_coords('arrsize_64_64_64_ntheta_500', i)
    # obj_rot = apply_rotation(obj, coord_old, 'arrsize_64_64_64_ntheta_500')
    obj_rot = tf_rotate(obj, theta_ls_tensor[i], interpolation='NEAREST')
    exiting = multislice_propagate(obj_rot[:, :, :, 0], obj_rot[:, :, :, 1], energy_ev, psize_cm)
    # exiting = tf.abs(exiting)
    return exiting

sess = tf.Session()

# read model
grid_delta = np.load('phantom/grid_delta.npy')
grid_beta = np.load('phantom/grid_beta.npy')
obj_init = np.zeros([img_dim, img_dim, img_dim, 2])
obj_init[:, :, :, 0] = grid_delta
obj_init[:, :, :, 1] = grid_beta
obj = tf.Variable(initial_value=obj_init, dtype=tf.float32)

# list of angles
theta_ls = -np.linspace(theta_st, theta_end, n_theta)
theta_ls_tensor = tf.constant(theta_ls, dtype='float32')

# create data file
f = h5py.File('data_diff_tf_360_birot_nn.h5', 'w')
grp = f.create_group('exchange')
dat = grp.create_dataset('data', shape=(n_theta, grid_delta.shape[0], grid_delta.shape[1]), dtype=np.complex64)

sess.run(tf.global_variables_initializer())

for i, theta in enumerate(theta_ls):

    print(i)
    wave = rotate_and_project(i, obj)
    wave = sess.run(wave)
    dat[i, :, :] = wave
    dxchange.write_tiff(np.abs(wave), 'diffraction_dat_tf/mag_{:05d}'.format(i), overwrite=True, dtype='float32')

f.close()