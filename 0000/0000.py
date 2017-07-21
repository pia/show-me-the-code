from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# front
#font = ImageFont.truetype('', 30)

# open image
imageFile = 'base.jpeg'
img = Image.open(imageFile)

# add number
draw = ImageDraw.Draw(img)
draw.text((150, 0), '666', (205, 51, 51))   # red
draw = ImageDraw.Draw(img)

# save
img.save('target.png')
img.show()