import streamlit as st
import plotly.graph_objs as go
import trimesh
import numpy as np
import tempfile
import os

def cross_product(v1, v2):
    return np.cross(v1, v2)

def calculate_dimensions(mesh,scale):
    if mesh is not None:
        vertices = mesh.vertices
        min_vals = vertices.min(axis=0)
        max_vals = vertices.max(axis=0)
        dimensions = max_vals - min_vals
        return dimensions
    return np.array([0, 0, 0])
def center_of_mass(vectors, masses):
    if len(vectors) != len(masses):
        return None
    total_mass = sum(masses)
    if total_mass == 0:
        return None
    return sum(m * v for v, m in zip(vectors, masses)) / total_mass

def add_mesh_to_fig(mesh, fig, color, translation, scale):
    if mesh is not None:
        vertices = mesh.vertices*scale + translation
        faces = mesh.faces 
        fig.add_trace(go.Mesh3d(x=vertices[:, 0], y=vertices[:, 1], z=vertices[:, 2],
                                i=faces[:, 0], j=faces[:, 1], k=faces[:, 2],
                                color=color, opacity=0.50))

def plot_vectors(vectors, masses, show_resultant, show_difference, show_cross, show_com, mesh1=None, mesh2=None, translation1=None, translation2=None):
    fig = go.Figure()
    add_mesh_to_fig(mesh1, fig, color='blue', translation=translation1,scale=scale1)
    add_mesh_to_fig(mesh2, fig, color='red', translation=translation2,scale=scale2)

    if show_resultant:
        resultant = np.add(vectors[0], vectors[1])
        fig.add_trace(go.Scatter3d(x=[0, resultant[0]], y=[0, resultant[1]], z=[0, resultant[2]],
                                   mode='lines+markers', name='resultant'))

    if show_difference:
        difference = np.subtract(vectors[0], vectors[1])
        fig.add_trace(go.Scatter3d(x=[0, difference[0]], y=[0, difference[1]], z=[0, difference[2]],
                                   mode='lines+markers', name='difference'))

    if show_cross:
        cross = cross_product(vectors[0], vectors[1])
        fig.add_trace(go.Scatter3d(x=[0, cross[0]], y=[0, cross[1]], z=[0, cross[2]],
                                   mode='lines+markers', name='cross product'))

    if show_com:
        com = center_of_mass(vectors, masses)
        if com is not None:
            fig.add_trace(go.Scatter3d(x=[com[0]], y=[com[1]], z=[com[2]],
                                       mode='markers', marker=dict(size=6, color='pink'), name='center of mass'))

    fig.update_layout(scene=dict(xaxis=dict(nticks=4, range=[-20,20]),
                                 yaxis=dict(nticks=4, range=[-20,20]),
                                 zaxis=dict(nticks=4, range=[-20,20])),
                      margin=dict(l=0, r=0, b=0, t=0))
    return fig

st.title('Interactive 3D Vector Plotter with OBJ Files and Position Adjustment')

mesh_file1 = st.file_uploader("Upload OBJ file for mesh 1", type=["obj"])
mesh_file2 = st.file_uploader("Upload OBJ file for mesh 2", type=["obj"])

translation1_x = st.slider('Mesh 1 Translation X', -10.0, 10.0, 0.0)
translation1_y = st.slider('Mesh 1 Translation Y', -10.0, 10.0, 0.0)
translation1_z = st.slider('Mesh 1 Translation Z', -10.0, 10.0, 0.0)
translation1 = np.array([translation1_x, translation1_y, translation1_z])

translation2_x = st.slider('Mesh 2 Translation X', -10.0, 10.0, 0.0, key='mesh2_x')
translation2_y = st.slider('Mesh 2 Translation Y', -10.0, 10.0, 0.0, key='mesh2_y')
translation2_z = st.slider('Mesh 2 Translation Z', -10.0, 10.0, 0.0, key='mesh2_z')
translation2 = np.array([translation2_x, translation2_y, translation2_z])

scale2 = st.slider('Mesh 2 scale', 0.1, 3.0, 0.0, key='mesh1_scale')
scale1 = st.slider('Mesh 2 scale', 0.1, 3.0, 0.0, key='mesh2_scale')

# Adjustments within the file handling section
if mesh_file1 is not None and mesh_file2 is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".obj") as temp_file1, tempfile.NamedTemporaryFile(delete=False, suffix=".obj") as temp_file2:
        temp_file1.write(mesh_file1.getvalue())
        temp_file2.write(mesh_file2.getvalue())
        # No need to manually close - the context manager handles this.

    # Ensure the file is closed by the context manager before proceeding.
    mesh1 = trimesh.load(temp_file1.name, file_type="obj", force = "mesh")
    mesh2 = trimesh.load(temp_file2.name, file_type="obj", force = "Mesh")
    dimension1 = calculate_dimensions(mesh1,scale1)
    dimension2 = calculate_dimensions(mesh2,scale2)
    # Delete temporary files after loading into trimesh
    try:
        os.unlink(temp_file1.name)
    except PermissionError as e:
        st.error(f"Error deleting temporary file: {e}")
    try:
        os.unlink(temp_file2.name)
    except PermissionError as e:
        st.error(f"Error deleting temporary file: {e}")

    show_resultant = st.checkbox('Show resultant (v1 + v2)', False)
    show_difference = st.checkbox('Show difference (v1 - v2)', False)
    show_cross = st.checkbox('Show cross product (v1 x v2)', False)
    show_com = st.checkbox('Show center of mass', False)

    if st.button('Plot Vectors'):
        # Use dimensions in your calculations here. For demonstration:
        # Let's say v1 and v2 are proportional to the dimensions of mesh1 and mesh2
        v1 = dimension1
        v2 = dimension2
        masses = [1, 1]  # Example masses, adjust as needed

        fig = plot_vectors([v1, v2], masses, show_resultant, show_difference, show_cross, show_com, mesh1=mesh1, mesh2=mesh2, translation1=translation1, translation2=translation2)
        st.plotly_chart(fig)
