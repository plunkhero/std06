#การตัดคำ tokenization + custom_Dict
import re
LEGAL_KEYWORD = ["ละเมิดสิทธิบัตร","เครื่องหมายการค้า","ลิขสิทธิ์","การกระทำความผิด","มาตรา"]

def legal_tokenizer(text):
    # ใช้ regx จัดการเบื้องต้น ค่อยตัดด้วยส่วนที่เหลือ
    compound = "|".join(map(re.escape,sorted(LEGAL_KEYWORD, key=len, reverse=True)))
    pattern = (compound + r"|\u0E00-\u0E7F"+ r"|a-zA-Z0-9")
    return re.findall(pattern, text)


test_text = "จำเลยกระทำความผิดฐานละเมิดสิทธิบัตรและเครื่องหมายการค้ามาตรา"
tokens = legal_tokenizer(test_text)
print(f"Input: {test_text}")
print(f"Output: {tokens}")


# ตัดคำด้วย deepcut 
# import deepcut
# print(f"Output Deepcut: {deepcut.tokenizer(test_text)}")