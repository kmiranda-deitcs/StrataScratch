import cv2
import os

# Set up variables
img_path = './/datasets//dog.jpg'   # Image path

# Fail if file does not exist
if not os.path.exists(img_path):
    raise FileNotFoundError('File not found. Please check image path: ' + img_path)

image = cv2.imread(img_path)        # Read image path and assign to 'image'
print('Image Path: ' + img_path)

# Set image to grayscale
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)     
# Invert the grayscale image
negative = cv2.bitwise_not(grayscale)                 
# Add blur to the inverted-grayscale image
blur = cv2.GaussianBlur(negative, (15, 15), 0)
# Finalizing the pencil sketch
sketch = cv2.divide(grayscale, blur, scale=256.0)        

#Show results
cv2.imshow('Original', image)
cv2.imshow('Sketch', sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()