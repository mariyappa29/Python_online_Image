from PIL import Image

img=Image.open('./Galaxy.jpg')
box=(1000,1000,4000,4000)
crop_image=img.crop(box)
crop_image.save("crop_image.png","png")
resize_image=img.resize((3000,2000))
resize_image.save('resixe_image.png','png')
