git init
# สร้าง Git repository ในโฟลเดอร์ปัจจุบัน (.git จะถูกสร้างขึ้น)

git status
# ตรวจสอบสถานะไฟล์ในโปรเจกต์
# ดูว่าไฟล์ไหนถูก track / ยังไม่ track / อยู่ใน staging หรือยัง

git commit -m "ข้อความอธิบาย"
# บันทึกการเปลี่ยนแปลงลง Git (ต้อง git add ก่อน)
# -m คือ message อธิบายว่า commit นี้ทำอะไร

git branch
# แสดงรายการ branch ทั้งหมดในเครื่อง (local)
# * คือ branch ที่กำลังใช้งานอยู่

git checkout feature/login
# เปลี่ยนไปยัง branch ชื่อ feature/login
# (branch นี้ต้องมีอยู่แล้ว ไม่งั้นจะ error)

git switch feature/login
# เหมือน checkout แต่เป็นคำสั่งใหม่ (อ่านง่ายกว่า)
# ใช้สำหรับสลับ branch

git checkout -b std06-w3
# สร้าง branch ใหม่ชื่อ feature/login และสลับไปใช้งานทันที

git merge feature/login
# รวม (merge) branch feature/login เข้ากับ branch ปัจจุบัน
# ต้องอยู่ branch ปลายทางก่อน เช่น main แล้วค่อย merge