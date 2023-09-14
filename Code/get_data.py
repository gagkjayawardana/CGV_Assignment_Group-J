import cv2
import pytesseract

img = cv2.imread('img.png')
img = cv2.resize(img, None, fx=1, fy=1, interpolation=cv2.INTER_CUBIC)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

adaptive_threshold = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)

config = '--psm 3'
text = pytesseract.image_to_string(adaptive_threshold, config=config)
print(text)

# cv2.imshow('image', img)
cv2.imshow('adaptive_threshold', adaptive_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()









