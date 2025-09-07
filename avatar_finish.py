from PIL import Image

red = Image.open("monro_red.jpg")
green = Image.open("monro_green.jpg")
blue = Image.open("monro_blue.jpg")
offset1 = 50
offset2 = 25
coordinates = ((offset1, 0, red.width, red.height))
red1 = red.crop(coordinates)
red.save("red_left.jpg")
coordinates = ((offset2, 0, red.width - offset2, red.height))
red2 = red.crop(coordinates)
print(red.size)
red.save("red_middle.jpg")
image1 = Image.blend(red1, red2, 0.5)
image1.save("red_monro.jpg")
coordinates = ((0, 0, blue.width - offset1, blue.height))
blue1 = blue.crop(coordinates)
blue.save("blue_right.jpg")
coordinates = ((offset2, 0, blue.width - offset2, blue.height))
blue2 = blue.crop(coordinates)
print(blue.size)
blue.save("blue_middle.jpg")
image2 = Image.blend(blue1, blue2, 0.5)
image2.save("blue_monro.jpg")
coordinates = ((offset2, 0, green.width - offset2, green.height))
green = green.crop(coordinates)
print(green.size)
green.save("green_monro.jpg")
red = Image.open("red_monro.jpg")
green = Image.open("green_monro.jpg")
blue = Image.open("blue_monro.jpg")
image = Image.merge("RGB", (red, green, blue))
image.save("monro_finish.jpg")
print(image.size)
image.thumbnail((80, 80))
image.save("monro_finish_thumbnail.jpg")
print(image.size)








