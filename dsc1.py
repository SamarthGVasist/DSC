import cv2
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img=Image.open(r"C:\Users\SAMARTH G VASIST\Downloads\IMG_20190605_131900.jpg")

text=pytesseract.image_to_string(img)
print(text)
