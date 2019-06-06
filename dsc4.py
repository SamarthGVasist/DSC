import pytesseract
from PIL import Image
 

img=Image.open("2.png");

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

result=pytesseract.image_to_string(img);

print(result);