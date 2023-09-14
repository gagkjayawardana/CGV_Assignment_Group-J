import cv2
import pytesseract
import xml.etree.ElementTree as ET

# Load the image
image_path = 'img.png'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Binarize the image 
binary_image = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
cv2.imshow('Binarized Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Perform OCR to extract text from the image
extracted_text = pytesseract.image_to_string(binary_image)

# Define the XML content with triple quotes
xml_content = 'info.xml'

# Load attendance data from the XML content
attendance_data = {}
root = ET.parse(xml_content).getroot()


for student in root.findall('.//student'):
    index = student.find('index').text
    name = student.find('name').text
    attendance_data[index] = name

# Process the OCR results to determine attendance
attendance = {}
for line in extracted_text.splitlines():
    for index, name in attendance_data.items():
        if index in line:
            attendance[name] = 'present'
            break
    else:
        attendance[name] = 'absent'

# Display the attendance results with index, name and status
for index, name in attendance_data.items():
    print(index, name, attendance[name])

# Close any open windows
cv2.destroyAllWindows()



