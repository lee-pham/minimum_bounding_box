import glob
import os
from PIL import Image

pngs = glob.glob('originals/*.png')

for png in pngs:
    im = Image.open(png)
    cropped_im = im.crop(im.convert('RGBa').getbbox())
    file_name = os.path.basename(png)
    cropped_im.save(f'cropped/{file_name}')
    print(f'Converted {png} to cropped/{file_name}')
