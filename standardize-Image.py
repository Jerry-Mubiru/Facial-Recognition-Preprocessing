import os
from PIL import Image

class ImageResize:
    @staticmethod
    def resize_image(image, size=(250, 250), dpi=96):
        # Resizing the image while preserving aspect ratio
        resized_image = image.copy()
        resized_image.thumbnail(size)
        # Creating a new image with the desired DPI
        new_image = Image.new('RGB', size, (255, 255, 255))
        new_image.paste(resized_image, ((size[0] - resized_image.width) // 2, (size[1] - resized_image.height) // 2))
        # Setting the DPI
        new_image.info['dpi'] = (dpi, dpi)

        return new_image

# Input and output directories
input_directory = 'Raw Images'
output_directory = 'Refined Images'
# Creating the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Looping through each file in the input directory
for filename in os.listdir(input_directory):
    # Checking if the file is a JPG image
    if filename.endswith('.jpg'):
        # Opening the image
        input_image = Image.open(os.path.join(input_directory, filename))
        # Resizing the image using the ImageResize class
        resized_image = ImageResize.resize_image(input_image)
        # Saving the resized image to the output directory
        output_path = os.path.join(output_directory, filename)
        resized_image.save(output_path)

        print(f"Resized {filename} and saved as {output_path}")

print("Resizing completed.")
