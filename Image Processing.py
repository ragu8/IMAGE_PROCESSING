from PIL import Image

# Loading the image
img = Image.open("Z:\GITHUB_REPOSITORIES\IMAGE_PROCESSING\me-and-myfriends.jpg")

# Understanding about image
print(img.format)
print(img.mode)
print(img.size)

# Resize
resize_img = img.resize((6000,4500))
print(resize_img.size)

# saving the resize image
resize_img.save("Z:\GITHUB_REPOSITORIES\IMAGE_PROCESSING\resize.jpg")