สิ่งที่ต้องติดตั้ง

macOS: brew install tesseract

Linux (Ubuntu): sudo apt install tesseract-ocr

เลือก version ล่าสุด
Windows: https://github.com/UB-Mannheim/tesseract/wiki

วิธีติดตั้งภาษาไทยใน Tesseract OCR บน Windows
  - ติดตั้ง Tesseract OCR (ถ้ายังไม่ได้ติดตั้ง): https://github.com/UB-Mannheim/tesseract/wiki

  - ตรวจสอบว่าไฟล์ภาษาไทยมีอยู่ในเครื่องแล้วหรือยัง
      ไปที่โฟลเดอร์ติดตั้งของ Tesseract OCR เช่น: C:\Program Files\Tesseract-OCR\tessdata\
    ดูว่ามีไฟล์ชื่อ tha.traineddata อยู่หรือไม่
    
  - ถ้ายังไม่มี ให้ดาวน์โหลดไฟล์ภาษาไทย
      ไปที่: https://github.com/tesseract-ocr/tessdata
    ดาวน์โหลดไฟล์ tha.traineddata
    วางไว้ในโฟลเดอร์: C:\Program Files\Tesseract-OCR\tessdata\

  - ตั้งค่าพาธในโค้ด Python ชื่อไฟล์ ocr_main.py
      import pytesseract
      from PIL import Image

      # ตั้งค่าที่อยู่ของ tesseract.exe ตรงนี้นะใน '####'
      pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

      # เปิดภาพและแปลงเป็นข้อความภาษาไทย
      img = Image.open('images/example.png')

      # ตรง lang='' สามารถกำหนดได้ว่าจะเอาภาษาอะไร ถ้าจะเอาอังกฤษอย่างเดียวให้แก้ตรง 'tha' เป็น 'eng'
      # ถ้า ไทย อย่างเดียว เป็น 'tha' ถ้าเอาทั้งสองเป็น 'eng+tha'
      text = pytesseract.image_to_string(img, lang='tha')  # ใช้ภาษาไทย
      print(text)
