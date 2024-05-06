import os
import cv2
import numpy as np

def histogram_normalization(image):
    # Convert image to LAB color space
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    
    # Split LAB image into channels
    l_channel, a_channel, b_channel = cv2.split(lab_image)
    
    # Apply histogram equalization to L channel
    l_channel_eq = cv2.equalizeHist(l_channel)
    
    # Merge channels back together
    normalized_lab_image = cv2.merge((l_channel_eq, a_channel, b_channel))
    
    # Convert LAB image back to BGR color space
    normalized_bgr_image = cv2.cvtColor(normalized_lab_image, cv2.COLOR_LAB2BGR)
    
    return normalized_bgr_image

# Path to the directory containing input images
input_directory = 'Raw Images'

# Path to the directory where output images will be saved
output_directory = 'Refined Images'

# Create output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Loop over each file in the input directory
for filename in os.listdir(input_directory):
    # Check if the file is a JPG image
    if filename.endswith('.jpg'):
        # Read the image
        input_image = cv2.imread(os.path.join(input_directory, filename))
        
        # Perform histogram normalization
        normalized_image = histogram_normalization(input_image)
        
        # Save the normalized image in the output directory
        output_path = os.path.join(output_directory, filename)
        cv2.imwrite(output_path, normalized_image)

        print(f"Processed {filename} and saved as {output_path}")

print("Processing completed.")
