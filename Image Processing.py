# import module
from PIL import Image

path = "Z:/GITHUB_REPOSITORIES/IMAGE_PROCESSING/image_samples/"

# Loading the image
img = Image.open(path +"myfriends.jpg")

# Understanding about image
print(img.format)
print(img.mode)
print(img.size)

# Resize
resize_img = img.resize((1000,1500))
print(resize_img.size)

# Saving the resize image
resize_img.save(path +"resize.jpg")

# Thumbnail
img.thumbnail((650,600))
img.save(path +"thumbnail.jpg")
print(img.size)

# Crop
img = Image.open(path +"myfriends.jpg")
cropped_img = img.crop((0,0,300,300)) 
img.save(path +"cropping.jpg")
print(cropped_img.size)

# copy
img_copy = img.copy()

# Image overlap
img1 = Image.open(path +"myfriends.jpg")
img2 = Image.open(path +"friends.png")
resize_img2 = img2.resize((1000,750))
img_overlap = img1.copy()
img_overlap.paste(resize_img2,(1000,1000))
img_overlap.save(path +"overlap.jpg")

# Image rotation
img_90 = img.rotate(90)
img_90.save(path +"rotation_90.jpg") 

img_45 = img.rotate(45)
img_45.save(path +"rotation_45.jpg")

img_180 = img.rotate(180)
img_180.save(path +"rotation_180.jpg")

img_8 = img.rotate(8)
img_8.save(path +"rotation_8.jpg")

# Flip
img_Left_to_Right = img.transpose(Image.FLIP_LEFT_RIGHT)
img_Left_to_Right.save(path +"flip_left_to_right.jpg")

img_top_to_buttom = img.transpose(Image.FLIP_TOP_BOTTOM)
img_top_to_buttom.save(path +"flip_top_to_buttom.jpg")

# Grayscale
grey_img = img.convert("L")
grey_img.save(path +"grey.jpg")


 








