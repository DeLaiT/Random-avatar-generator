import random
from PIL import Image

size = 8
seed = input("username: ")
random.seed(seed)

c_full = random.randint(0, 2)
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

if c_full == 0:
    r = 255
elif c_full == 1:
    g = 255
else:
    b = 255

if random.randint(0, 1) == 0:
    color1 = (r, g, b)
    color2 = (int(r/2), int(g/2), int(b/2))
else:
    color2 = (r, g, b)
    color1 = (int(r/2), int(g/2), int(b/2))

img = Image.new('RGB', (size, size), color1)

pixels = img.load()
for y in range(size):
    for x in range(int(size/2)):
        if random.randint(0, 1) == 0:
            pixels[x, y] = color2
            pixels[size-1-x, y] = color2

img.save("av.png")



