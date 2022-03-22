import sys
import os
from PIL import Image

#  python3 3.converter.py Pokedex/ new/
#  grab the first and second arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#  check if new folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#  loop through all the image
#  convert images to png
for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}{filename}")
    clean_name = os.path.splitext(filename)[0]  # separate filename and .jpeg
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')


#  save them to the new folder
