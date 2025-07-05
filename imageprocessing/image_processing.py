from PIL import Image, ImageFilter

img = Image.open("clcoding.jpg")
img.show()

blur_img = img.filter(ImageFilter.BLUR)
blur_img.show()

gray_img = img.convert('L')
gray_img.show()

edge_img = img.filter(ImageFilter.FIND_EDGES)
edge_img.show() 