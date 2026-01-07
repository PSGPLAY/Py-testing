from PIL import Image, ImageEnhance, ImageFilter
import os

path = "toEdit/"
pathout = "edited/"

for filename in os.listdir(path):
   img = Image.open(f"{path}/{filename}")

   edit = img.filter(ImageFilter.SHARPEN).convert("L")
   

   clean_name = os.path.splitext(filename)[0]

   edit.save(f"{pathout}/{clean_name}edited.jpg")