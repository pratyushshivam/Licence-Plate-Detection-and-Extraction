import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img  = Image.open("image__to__extract.png")
text = pytesseract.image_to_string(img) #It will convert to strings
print(text)