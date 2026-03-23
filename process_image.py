from rembg import remove
from PIL import Image
import os
input_path = 'C:/Users/hamza/Desktop/Personal/Portfolio/48730d7d-7461-42b5-a9a9-f3d6ddbc9a43.jpg'
output_path = 'C:/Users/hamza/Desktop/Personal/Portfolio/static/images/hero-photo-transparent.png'
try:
    input_image = Image.open(input_path)
    output_image = remove(input_image)
    output_image.save(output_path)
    print('Background removed successfully.')
except Exception as e:
    print(f'Error: {e}')
