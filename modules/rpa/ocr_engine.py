
import pytesseract  #Python wrapper for Google's Tesseract-OCR Engine
from PIL import Image
import cv2 #For image processing and manipulation
import os #To check file paths and system access

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):

    '''Function to extract text from an image using OCR:
    1. Checks if the image file exists
    2. Reads the image using OpenCV
    3. Converts the image to grayscale (better for OCR accuracy)
    4. Feeds the grayscale image into Tesseract to extract text
    5. Returns the extracted text'''

    if not os.path.exists(image_path):
        return "Image not found."

    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

if __name__ == "__main__":
    path = "bonafied.jpg"  
    result = extract_text_from_image(path)
    print("\n!OCR Result:\n")
    print(result)
