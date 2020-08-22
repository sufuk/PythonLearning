# Improting Image class from PIL module
from PIL import Image

# Opens a image in RGB mode
im = Image.open(r"C:\Users\Sufuk\Desktop\PythonLearning\image.png")

# Size of the image in pixels (size of orginal image)
# (This is not mandatory)
width, height = im.size

# Setting the points for cropped image
left1 = 450
top1 = 10
right1 = 800
bottom1 = 70

# Cropped image of above dimension
# (It will not change orginal image)
im1 = im.crop((left, top, right, bottom))

# Shows the image in image viewer
im1.save("mal.png")
