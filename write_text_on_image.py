from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

for i in range(1,62):
    img = Image.open("D:\\Work2021\AutoRotation\\image_data\\all\\"+str(i)+".bmp")
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("C:\\WINDOWS\\FONTS\\CALIBRIL.ttf", 100)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((10, 10),str(i),(255,0,0),font)
    img.save(str(i)+".bmp")
