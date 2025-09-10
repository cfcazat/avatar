from PIL import Image

offset1 = 50
offset2 = 25
image = Image.open("monro.jpg")
r, g, b = image.split()

r1 = r.crop((offset1, 0, r.width, r.height))
r2 = r.crop((offset2, 0, r.width - offset2, r.height))
red1 = Image.blend(r1, r2, 0.5)

b1 = b.crop((0, 0, b.width - offset1, b.height))
b2 = b.crop((offset2, 0, b.width - offset2, b.height))
blue2 = Image.blend(b1, b2, 0.5)

green3 = g.crop((offset2, 0, g.width - offset2, g.height))

image = Image.merge("RGB", (red1, green3, blue2))
image.save("monro_finish.jpg")

image.thumbnail((80, 80))
image.save("monro_finish_thumbnail.jpg")










