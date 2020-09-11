from PIL import Image
im = Image.open(r"C:\Users\Sufuk\Desktop\PythonLearning\image.png")
width, height = im.size
left1 = 450
top1 = 10
right1 = 800
bottom1 = 70
im1 = im.crop((left, top, right, bottom))
im1.save("mal.png")
