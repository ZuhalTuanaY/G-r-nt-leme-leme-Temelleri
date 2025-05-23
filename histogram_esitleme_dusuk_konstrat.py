import cv2
import matplotlib.pyplot as plt

img = cv2.imread("C://Users//BL4CKE4RTH//Downloads//istanbul-4917450_1280.jpg", cv2.IMREAD_GRAYSCALE)

equalized_img = cv2.equalizeHist(img) # Bu fonksiyon, histogram eşitleme uygular. Histogram eşitleme, görüntünün parlaklık dağılımını daha homojen ve geniş bir aralığa yayarak kontrastını artırmaya yarar.

# Orijinal ve eşitlenmiş görüntüyü göster
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("Orijinal Görüntü")
plt.imshow(img, cmap='gray')

plt.subplot(1,2,2)
plt.title("Histogram Eşitlenmiş Görüntü")
plt.imshow(equalized_img, cmap='gray')

plt.show()

# Histogramları çiz
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.hist(img.ravel(), bins=256, range=[0,256])
plt.title('Orijinal Histogram')

plt.subplot(1,2,2)
plt.hist(equalized_img.ravel(), bins=256, range=[0,256])
plt.title('Eşitlenmiş Histogram')

plt.show()


color_img = cv2.imread("C://Users//BL4CKE4RTH//Downloads//istanbul-4917450_1280.jpg")
ycrcb = cv2.cvtColor(color_img, cv2.COLOR_BGR2YCrCb)

# Sadece Y(parlaklık) kanalına histogram eşitleme uygula
ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])

# Tekrar BGR formatına çevir
result = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow("Renkli Görüntü (Eşitlenmiş)", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

