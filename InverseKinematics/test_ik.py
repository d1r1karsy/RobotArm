#!/usr/bin/env python
# coding: utf-8
import ikpy
import numpy as np
from ikpy import plot_utils

my_chain = ikpy.chain.Chain.from_urdf_file("./niryo_one.urdf")

#target_vector = [ 0.1, -0.2, 0.1]
#target_vector = [ 0.3, -0.3, 0.3]
target_vector = [4, 4, 4]
target_frame = np.eye(4)
target_frame[:3, 3] = target_vector
#print(target_frame)

angles = my_chain.inverse_kinematics(target_frame)
print("The angles of each joints are :")
for i in range(len(angles)):
    print(angles[i])

real_frame = my_chain.forward_kinematics(angles)
print("Computed position vector : %s, original position vector : %s" % (real_frame[:3, 3], target_frame[:3, 3]))

# %matplotlib notebook
import matplotlib.pyplot as plt
ax = plot_utils.init_3d_figure()
my_chain.plot(my_chain.inverse_kinematics(target_frame), ax, target=target_vector)
plt.xlim(-0.1, 0.1)
plt.ylim(-0.1, 0.1)
