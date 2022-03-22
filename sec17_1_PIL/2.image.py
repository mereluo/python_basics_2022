from PIL import Image

img = Image.open('astro.jpeg')
img.thumbnail((400, 400))  # not changing the ratio
img.save('thumbnail.jpg')
print(img.size)  # (400, 380)
