import cv2 as cv

img = cv.imread('0_data/dog_img1.jpg')


cv.imshow('Dog Image', img)

# Store/Save the image
img_name = "0_data/Dog_Image.jpg"
cv.imwrite(img_name, img)
# 0 means the image will be displayed till any key is pressed
cv.waitKey(0)

# close ll the windows
cv.destroyAllWindows()