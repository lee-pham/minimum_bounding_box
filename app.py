import glob
import os
from PIL import Image

pngs = glob.glob(r'originals/*.png')

for i, png in enumerate(pngs):
    im = Image.open(png)
    cropped_im = im.crop(im.convert('RGBa').getbbox())
    cropped_im.save(f'cropped/{os.path.basename(png)}')
    print(f'Converted {png} to cropped/{os.path.basename(png)}')
