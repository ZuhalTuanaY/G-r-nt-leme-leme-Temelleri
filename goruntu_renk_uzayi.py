import cv2
import matplotlib.pyplot as plt

# Görüntüyü oku (BGR formatında)
image = cv2.imread("C://Users//BL4CKE4RTH//Downloads//ornek (1).jpg")  # Buraya kendi görselinin adını yaz

# BGR'den RGB'ye çevir
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# BGR'den Grayscale (gri tonlamalı) formata çevir
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# BGR'den HSV renk uzayına çevir
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_hsv_rgb = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB)  # HSV görüntüyü matplotlib'te göstermek için RGB'ye çevir

# Görselleri karşılaştırmak için yan yana göster
plt.figure(figsize=(15, 5))#15 genişlik, 5 yükseklik

# RGB
plt.subplot(1, 3, 1)#1 satır 3 sutunluk yerleşkede ilk resim
plt.imshow(image_rgb)
plt.title("RGB")
plt.axis('off')

# Grayscale
plt.subplot(1, 3, 2)#1 satır 3 sutunluk yerleşkede ikinci resim
plt.imshow(image_gray, cmap='gray')
plt.title("Grayscale")
plt.axis('off')

# HSV
plt.subplot(1, 3, 3)#1 satır 3 sutunluk yerleşkede üçüncü resim
plt.imshow(image_hsv_rgb)
plt.title("HSV")
plt.axis('off')

plt.tight_layout()# Grafik elemanlarının üst üste binmesini engeller.
plt.show()#Tüm grafikleri bir pencerede gösterir.
