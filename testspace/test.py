from PIL import Image
import os



p='ps4controller.jpg'
s='ps4controlleredit.jpg'


img = Image.open(p)
new_img = (400, 400)
img.thumbnail(new_img)
img.save(s)