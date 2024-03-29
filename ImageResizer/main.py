import cv2

# Configurable parameters
source = "aest.jpg"
destination = "newImage.jpg"
# percent by which image is resized
scale_percent = 50

image = cv2.imread(source, cv2.IMREAD_UNCHANGED)

# calculate the 50 percent of original dimensions
new_width = int(image.shape[1] * scale_percent/100)
new_height = int(image.shape[0] * scale_percent/100)

# resize image
output = cv2.resize(image, (new_width, new_height))

cv2.imwrite(destination, output)
cv2.waitKey(0)