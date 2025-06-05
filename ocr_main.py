from PIL import Image
import pytesseract
import os

# กำหนด path ของ tesseract.exe ถ้าใช้บน Windows 
# ต้องโหลดด้วยนะของ Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text(image_path):
    try:
        # เปิดภาพ
        img = Image.open(image_path)

        # ใช้ pytesseract อ่านข้อความจากภาพ
        text = pytesseract.image_to_string(img, lang='eng+tha')  # หรือ 'tha' ถ้าเป็นภาษาไทย

        return text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    image_file = "images/ReceiptSwiss.jpg"
    
    if os.path.exists(image_file):
        result = image_to_text(image_file)
        print("📄 Text from image:")
        print(result)
    else:
        print(f"❌ Image not found: {image_file}")
