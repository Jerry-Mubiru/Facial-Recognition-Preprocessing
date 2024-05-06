import os
import face_alignment
from skimage import io
import numpy as np
from scipy.spatial import Delaunay

# Path to the directory containing your .jpg files
directory = 'Refined Images'

# List all files in the directory
files = os.listdir(directory)

# Filter for files ending in .jpg
jpg_files = [file for file in files if file.endswith('.jpg')]

# Optionally set detector and some additional detector parameters
face_detector = 'sfd'
face_detector_kwargs = {
    "filter_threshold": 0.8
}

# Initialize the face alignment with 3D landmarks
fa = face_alignment.FaceAlignment(face_alignment.LandmarksType.THREE_D, device='cpu', flip_input=True,
                                  face_detector=face_detector, face_detector_kwargs=face_detector_kwargs)

# Loop over each .jpg file
for filename in jpg_files:
    # Full path to image
    image_path = os.path.join(directory, filename)
    
    # Read the image
    input_img = io.imread(image_path)

    # Get landmarks
    preds = fa.get_landmarks(input_img)
    if preds is None:
        print(f"No landmarks detected in {filename}.")
        continue

    # Extract the last set of landmarks (assuming it's the desired face if multiple are detected)
    preds = preds[-1]

    # Define the vertices of the mesh using the landmarks
    vertices = preds
    
    # Triangulate the vertices to form triangular faces
    tri = Delaunay(vertices[:, :2])  # Triangulate only using x and y coordinates
    
    # Generate texture coordinates based on landmark positions
    texture_coords = vertices[:, :2] / input_img.shape[1]
    
    # Save the vertices, texture coordinates, and faces as an OBJ file with corresponding MTL file
    obj_filename = filename.replace('.jpg', '.obj')
    mtl_filename = filename.replace('.jpg', '.mtl')
    with open(os.path.join(directory, obj_filename), 'w') as obj_file:
        obj_file.write("# Vertices\n")
        for vertex, tex_coord in zip(vertices, texture_coords):
            obj_file.write(f"v {vertex[0]} {vertex[1]} {vertex[2]}\n")
            obj_file.write(f"vt {tex_coord[0]} {tex_coord[1]}\n")
        
        obj_file.write("\n# Faces\n")
        for face in tri.simplices:
            obj_file.write(f"f {face[0]+1}/{face[0]+1} {face[1]+1}/{face[1]+1} {face[2]+1}/{face[2]+1}\n")
    
    # Create MTL file
    with open(os.path.join(directory, mtl_filename), 'w') as mtl_file:
        mtl_file.write("newmtl material_0\n")
        mtl_file.write("Ka 1.0 1.0 1.0\n")
        mtl_file.write("Kd 1.0 1.0 1.0\n")
        mtl_file.write("Ks 0.0 0.0 0.0\n")
        mtl_file.write("d 1.0\n")
        mtl_file.write("illum 2\n")
        mtl_file.write(f"map_Kd {filename}\n")
