from PIL import Image, ImageFilter

img = Image.open('Pokedex/pikachu.jpeg')

print(img.format)  # jpeg
print(img.size)  # (640, 640)
print(img.mode)  # RGB

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", 'png')
filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save("smooth.png", 'png')
filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save("sharpen.png", 'png')
filtered_img = img.convert('L')
filtered_img.save('bnw.png', 'png')
# filtered_img.show()
# filtered_img.rotate(90)
# filtered_img.resize((300, 300))
# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
