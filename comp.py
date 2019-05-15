from PIL import Image
import io, os, sys
import requests
from bs4 import BeautifulSoup

r = requests.get("https://shop.techsmartgifts.com/ez-posture-info/")
data = r.text
#print(data)
soup = BeautifulSoup(data, 'lxml')
main = soup.find("div", {"id": "sMain-Advertorial"})
sidebar = soup.find("div", {"id": "sidebar-advertorial"})
print(main)
print(sidebar)

main.repace("")


path = "laser_files/"
dirs = os.listdir( path )
final_size = 700;
fileext = '.jpg'
print(dirs)
def resize_aspect_fit():

    for item in dirs:
         if item == '.DS_Store':
             continue 
         if os.path.isfile(path+item):
            filename, ext = os.path.splitext(item)
            if ext == fileext:
                 ogsize = (os.stat(path+item).st_size/1000)
                 print(ogsize)
                 if ogsize > 300:
                     print("yes")
                     im = Image.open(path+item)
                     f, e = os.path.splitext(path+item)
                     size = im.size
                     ratio = float(final_size) / max(size)
                     new_image_size = tuple([int(x*ratio) for x in size])
                     im = im.resize(new_image_size, Image.ANTIALIAS)
                     new_im = Image.new("RGB", (final_size, final_size))
                     new_im.paste(im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
                     new_im.save(f + '.jpg', 'JPEG', quality=70)
resize_aspect_fit()
print("done")