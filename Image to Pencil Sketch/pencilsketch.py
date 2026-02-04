import cv2
import os

# Set up variables
img_path = './/datasets//dlog.jpg'   # Image path

# Only run if file exists
if not os.path.exists(img_path):
    raise FileNotFoundError('File not found. Please check image path: ' + img_path)

image = cv2.imread(img_path)        # Read image path and assign to 'image'
print('Image Path: ' + img_path)

grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)     # Set image to grayscale

negative = cv2.bitwise_not(grayscale)                   # Invert the grayscale image

blur = cv2.GaussianBlur(negative, (15, 15), 0)          # Add blur to the inverted-grayscale image

sketch = cv2.divide(grayscale, blur, scale=256.0)        # Finalizing the pencil sketch

cv2.imshow('Original', image)
cv2.imshow('Sketch', sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()