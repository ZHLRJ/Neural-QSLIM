# -*- coding: utf-8 -*-
'''
@Time    : 2/5/25 
@Author  : Zhang Haoliang
'''
import pickle
from include import *
from psbody.mesh import Mesh, MeshViewers
import numpy as np
ex_mesh = 'data_meshes/zhl_objs_original/dfaust_template.ply'
mesh = Mesh(filename = ex_mesh)
# Create a MeshViewer instance 3072 × 1920

with open('sample_info.pkl','rb') as f:
    sample_info = pickle.load(f)

# M = sample_info['D']
# Dm1 = D[2].toarray()

# up_trans_matrix = sample_info['U']
# m0  = up_trans_matrix[0].toarray()
# bottleneck_mesh = sample_info['M'][-1]
# trans = up_trans_matrix[-1].toarray()
# v1 = up_trans_matrix[-1]@bottleneck_mesh.v
# f1 =
# mesh1 = Mesh


upsample_meshes = [sample_info['M'][-1]]
v = sample_info['M'][-1].v
tgp.writeOBJ('dfaust/' + 'upsample' + '_' + str(len(v)) + '.obj',sample_info['M'][-1].v, sample_info['M'][-1].f)
for i,trans in enumerate(sample_info['U'][::-1],1):
    v = trans@v
    upsample_mesh = Mesh(v = v, f = sample_info['M'][-i-1].f )
    tgp.writeOBJ('dfaust/' + 'upsample' + '_' + str(len(v)) + '.obj', upsample_mesh.v, upsample_mesh.f)
    upsample_meshes.append(upsample_mesh)


# Show downsample mesh
def show_mesh(mesh_list):
    viewer = MeshViewers(shape = (1,5),window_width=3072,window_height=1920)
    for i in range(5):
        viewer[0][i].set_background_color(np.array([1., 1., 1.]))
        viewer[0][i].set_dynamic_meshes([mesh_list[i]])
    # viewer[0][1].set_background_color(np.array([1., 1., 1.]))
    # viewer[0][1].set_dynamic_meshes([mesh])
# show_mesh(upsample_meshes)