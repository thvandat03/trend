import sys
from PIL import Image
import time
# Đường dẫn file
#Lưu ảnh trong Folder PICTURES
head_path = './PICTURES'
# Khai báo tên ảnh: '\ + tên ảnh '
name_images = [
    '\pic1' , # '\tênảnh2'
    ]
# Phần mở rộng ảnh
extension_path = '.jpg'

for i in name_images:
    path_image = head_path + i + extension_path
    print('\n')
    for j in range(1):
        img = Image.open(path_image)
        
        width, height = img.size
        photo_ratio = height / width
        
        new_width = 120
        new_height = photo_ratio * new_width * 0.55
        
        img = img.resize((new_width, int(new_height)))
        img = img.convert('P')
        
        pixels = img.getdata()
        
        chars = [".","&","'",")",";","$","%","*","!",":","."]
        
        new_pixels = [chars[pixel//25] for pixel in pixels]
        new_pixels = ''.join(new_pixels)
        
        new_pixels_count = len(new_pixels)
        
        out_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
        out_image = "\n".join(out_image)
        
        print(out_image)
        time.sleep(0.75)
        
         
        
