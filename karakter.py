import cv2
import numpy as np
import os

# Pastikan folder output ada
os.makedirs("output", exist_ok=True)

# ---------- 1. Membuat Kanvas & Gambar Rumah Lilis ----------
canvas = np.full((500, 600, 3), (255, 255, 255), dtype=np.uint8)

# Lantai 1
cv2.rectangle(canvas, (150, 250), (450, 450), (200, 150, 100), -1)
# Lantai 2
cv2.rectangle(canvas, (200, 120), (400, 250), (210, 160, 110), -1)
# Atap segitiga
pts = np.array([[180, 120], [300, 40], [420, 120]], np.int32)
cv2.fillPoly(canvas, [pts], (100, 50, 0))
# Pintu
cv2.rectangle(canvas, (270, 340), (330, 450), (100, 60, 30), -1)
cv2.circle(canvas, (320, 400), 5, (0, 0, 0), -1)
# Jendela lantai 1 (kiri-kanan)
cv2.rectangle(canvas, (180, 300), (230, 350), (255, 255, 255), -1)
cv2.rectangle(canvas, (370, 300), (420, 350), (255, 255, 255), -1)
# Jendela lantai 2
cv2.rectangle(canvas, (270, 150), (330, 200), (255, 255, 255), -1)
cv2.line(canvas, (300, 150), (300, 200), (0, 0, 0), 2)
cv2.line(canvas, (270, 175), (330, 175), (0, 0, 0), 2)
# Teks bawah
cv2.putText(canvas, "RUMAH LILIS", (160, 490), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 3)

cv2.imwrite("output/karakter.png", canvas)

# ---------- 2. Transformasi ----------
rows, cols = canvas.shape[:2]

# Translasi
M_translate = np.float32([[1, 0, 60], [0, 1, 40]])
translated = cv2.warpAffine(canvas, M_translate, (cols, rows))
cv2.imwrite("output/translate.png", translated)

# Rotasi
M_rotate = cv2.getRotationMatrix2D((cols/2, rows/2), 25, 1)
rotated = cv2.warpAffine(canvas, M_rotate, (cols, rows))
cv2.imwrite("output/rotate.png", rotated)

# Resize
resized = cv2.resize(canvas, (300, 250))
cv2.imwrite("output/resize.png", resized)

# Crop
cropped = canvas[150:400, 200:450]
cv2.imwrite("output/crop.png", cropped)

# ---------- 3. Operasi Bitwise & Aritmatika ----------
# Buat background polos (biru muda)
bg = np.full_like(canvas, (180, 220, 255))

# Bitwise AND
bitwise_and = cv2.bitwise_and(canvas, bg)
cv2.imwrite("output/bitwise.png", bitwise_and)

# Gabungan akhir dengan efek transparan
final = cv2.addWeighted(canvas, 0.7, bg, 0.3, 0)
cv2.imwrite("output/final.png", final)

print("✅ Semua langkah selesai! Cek folder output untuk semua hasil.")
