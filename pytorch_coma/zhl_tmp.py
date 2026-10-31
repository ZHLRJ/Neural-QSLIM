# -*- coding: utf-8 -*-
'''
@Time    : 2/5/25 
@Author  : Zhang Haoliang
'''
import os
import sys

cwd = os.getcwd()
sys.path.append(cwd + '/pytorch_coma/')

import argparse
import os
import torch
import numpy as np
import torch.nn.functional as F
from torch_geometric.data import DataLoader

from psbody.mesh import Mesh, MeshViewers
import mesh_operations

import pickle
template_file_path = 'data_meshes/zhl_objs_original/dfaust_template.ply'
template_mesh = Mesh(filename=template_file_path)

downsampling_factors = [4,4,4,4]
M, A, D, U = mesh_operations.generate_transform_matrices(template_mesh, downsampling_factors)
# sample_info = {'M':M,'A':A,'D':D,'U':U}
# with open('sample_info.pkl','wb') as f:
#     pickle.dump(sample_info,f)

# v = template_mesh.v
# f = template_mesh.f

