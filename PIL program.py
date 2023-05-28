from PIL import Image
photo = Image.open("battlefield.jpg")
photo.show()

photo_2 = photo.convert('L')
photo_2.show()

samaler_photo = photo.resize((300,300))
samaler_photo.show()

box = (300,300,850,850)
area = photo.crop(box)
area.show()

rotation_photo = photo.rotate(60)
rotation_photo.show()