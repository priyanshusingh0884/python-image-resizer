import cv2

# Configurable Parameters
source = "harry.jpeg"
destination = "newImage.png"
scale_percent = 50  # Percent by which the image is resized

# cv2.imshow("title", src)
src  =  cv2.imread(source,cv2.IMREAD_UNCHANGED)
if src is None:
    print("Error: Could not load the image.")
    exit()


# Calculate the 50 percent of original dimensions
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# resize image
output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination, output)

# cv2.waitKey(0)