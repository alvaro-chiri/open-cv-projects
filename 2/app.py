import cv2
import numpy as np

# Load the image
image = cv2.imread('sampleImg.jpeg')

# Convert the image from BGR to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the color range for isolation (Example: Blue color)
# Adjust the range according to the color you want to isolate
lower_color = np.array([35, 150, 0])  # Lower range for blue
upper_color = np.array([140, 255, 255])  # Upper range for blue

# Define the color range for isolating green
lower_green = np.array([35, 100, 50])  # Lower range for green
upper_green = np.array([85, 255, 255])  # Upper range for green

# Define the color range for isolating the sky (blue colors)------this one was pretty bad
lower_sky = np.array([100, 150, 0])   # Lower range for sky blue
upper_sky = np.array([140, 255, 255])  # Upper range for sky blue

# Create a mask that isolates the colors in the specified range
mask = cv2.inRange(hsv_image, lower_color, upper_color)
#mask = cv2.inRange(hsv_image, lower_sky, upper_sky)
#mask = cv2.inRange(hsv_image, lower_green, upper_green)

# Apply the mask to the original image to extract the isolated color
filtered_image = cv2.bitwise_and(image, image, mask=mask)

# Optionally, you can manipulate the isolated color, like intensifying it
# Here we just display the masked image for now

# Show the original and the filtered image
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
