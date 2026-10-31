# -*- coding: utf-8 -*-
'''
@Time    : 2/5/25 
@Author  : Zhang Haoliang
'''
import polyscope as ps
from psbody.mesh import Mesh, MeshViewers
# Initialize polyscope
ps.init()

### Register a point cloud
# `my_points` is a Nx3 numpy array
# ps.register_point_cloud("my points", my_points)

### Register a mesh
# `verts` is a Nx3 numpy array of vertex positions
# `faces` is a Fx3 array of indices, or a nested list
template_file_path = 'data_meshes/cartoon_elephant_200/subd0/004.obj'
template_mesh = Mesh(filename=template_file_path)
verts, faces = template_mesh.v, template_mesh.f
ps.register_surface_mesh("my mesh", verts, faces, smooth_shade=True,edge_width=0.9,color=(0.836, 0.847, 0.858))
ps.set_ground_plane_mode('none')


# Add a scalar function and a vector function defined on the mesh
# vertex_scalar is a length V numpy array of values
# face_vectors is an Fx3 array of vectors per face
# ps.get_surface_mesh("my mesh").add_scalar_quantity("my_scalar",
#         vertex_scalar, defined_on='vertices', cmap='blues')
# ps.get_surface_mesh("my mesh").add_vector_quantity("my_vector",
#         face_vectors, defined_on='faces', color=(0.2, 0.5, 0.5))

# View the point cloud and mesh we just registered in the 3D UI
ps.show()