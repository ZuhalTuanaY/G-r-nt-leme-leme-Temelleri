import cv2
import matplotlib.pyplot as plt

# Görüntüyü yükle (renkli ya da gri olabilir)
image_path = "C://Users//BL4CKE4RTH//Downloads//1160x650-islamda-hayvan-sevgisi-1612273395839.jpg"  # Buraya kendi görüntü yolunu yaz
img = cv2.imread(image_path)

# Eğer renkli ise griye çevir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Canny Edge Detection uygulama
edges = cv2.Canny(gray, 100, 200) 
# 100 ve 200 eşik değerleri, değiştirerek farklı sonuçlar alabilirsin


# Görüntüyü yükle (renkli ya da gri olabilir)
image_path2 = "C://Users//BL4CKE4RTH//Downloads//sonuc (5).png" 
img2 = cv2.imread(image_path2)

# Eğer renkli ise griye çevir
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Canny Edge Detection uygulama
edges2 = cv2.Canny(gray, 100, 180) #Max değer azaltıldıkça, keskin piksellerde daha fazla kenar tespiti yapılır
# 100 ve 200 eşik değerleri, değiştirerek farklı sonuçlar alabilirsin

# Sonuçları görselleştir
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title('Orijinal Görüntü')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1,2,2)
plt.title('Canny Kenar Tespiti')
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.show()


# Sonuçları görselleştir
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title('Orijinal Görüntü')
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1,2,2)
plt.title('Canny Kenar Tespiti')
plt.imshow(edges2, cmap='gray')
plt.axis('off')

plt.show()

