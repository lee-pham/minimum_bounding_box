import glob
from PIL import Image


pngs = glob.glob("raw/*.png")

for i, png in enumerate(pngs):
    print("Converted " + png + " to cropped/" + str(i) + ".png")
    im = Image.open(png)
    cropped_im = im.crop(im.convert("RGBa").getbbox())
    cropped_im.save("cropped/" + str(i) + ".png")
