from deep_translator import GoogleTranslator
from PIL import Image
import pytesseract

im_file = "/content/data/test2.jpg"

im = Image.open(im_file)

ocr_result = pytesseract.image_to_string(im)

t_text = GoogleTranslator(source='auto', target='hi').translate(ocr_result)
print(t_text)
