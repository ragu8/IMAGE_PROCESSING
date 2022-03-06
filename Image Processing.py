from PIL import Image

# Loading the image
img = Image.open("Z:/GITHUB_REPOSITORIES/IMAGE_PROCESSING/myfriends.jpg")

# Understanding about image
print(img.format)
print(img.mode)
print(img.size)

# Resize
resize_img = img.resize((1000,1500))
print(resize_img.size)

# Saving the resize image
resize_img.save("Z:/GITHUB_REPOSITORIES/IMAGE_PROCESSING/resize.jpg")

# Thumbnail
img.thumbnail((650,600))
img.save("Z:/GITHUB_REPOSITORIES/IMAGE_PROCESSING/thumbnail.jpg")
print(img.size)

# Crop
img = Image.open("Z:/GITHUB_REPOSITORIES/IMAGE_PROCESSING/myfriends.jpg")
cropped_img = img.crop((0,0,300,300)) 
img.save("Z:/GITHUB_REPOSITORIES/IMAGE_PROCESSING/cropping.jpg")
print(cropped_img.size)

# copy
img_copy = img.copy()

# Image overlap
img1 = Image.open("Z:/GITHUB_REPOSITORIES/IMAGE_PROCESSING/myfriends.jpg")
img2 = Image.open("Z:/GITHUB_REPOSITORIES/IMAGE_PROCESSING/myfriends.jpg"))
img_overlap = img1.copy()
img_overlap.paste(img2,(50,50))
img_overlap.save("Z:/GITHUB_REPOSITORIES/IMAGE_PROCESSING/overlap.jpg")



















