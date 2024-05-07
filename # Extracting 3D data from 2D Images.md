# Extracting 3D data from 2D Images

## Overview
This part of the project consists of two scripts for face landmark detection: `face-landmark-detection.py` and `standardize-Image.py`. These scripts are designed to detect facial landmarks in images and visualize them through 2D and 3D plots.

## Prerequisites
Before running the scripts, ensure you have the following dependencies installed:
- Python 3.x
- face_alignment
- matplotlib
- scikit-image
- pillow

You can install these dependencies using pip:
```bash
pip install face_alignment matplotlib scikit-image pillow
```

## Usage

### Step 1: Standardize Images
1. Place the images you want to process in the `Raw Images` folder.
2. Run the `standardize-Image.py` script.
3. The script will resize the images to a standard size and save them in the `Refined Images` folder with a DPI of 96.

### Step 2: Detect Landmarks
1. After standardizing the images, run the `face-landmark-detection.py` script.
2. The script will detect facial landmarks in each image from the `Refined Images` folder.
3. It will generate 2D and 3D plots displaying the detected landmarks.

## Additional Information
- Both scripts assume that the images are in JPG format.
- Ensure that the `Raw Images` and `Refined Images` folders are in the same directory as the scripts.
- You can upload additional images to the `Raw Images` folder for processing.