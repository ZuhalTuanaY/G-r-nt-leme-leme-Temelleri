import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("C://Users//BL4CKE4RTH//Downloads//ornek (1).jpg")  # Buraya kendi görselinin adını yaz
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#Salt and pepper gürültüsü ekleniyor.Görüntüye rastgele yerlerde siyah yada beyaz yapar.
def salt_pepper_noise(image, oran):#görüntü ve gürültü oranı
    noisy = np.copy(image)#görüntü kopyalandı
    black = 0
    white = 255

    probs = np.random.rand(*image.shape[:2])#rastgele sayı üretir.
    noisy[probs < oran] = black #Eğer rastgele sayı oran’dan küçükse, o piksel siyah (0) yapılır.
    noisy[probs > 1 - oran] = white #Eğer rastgele sayı 1 - oran’dan büyükse, o piksel beyaz (255) yapılır.
    return noisy

# Gaussian Gürültüsü
def gaussian_noise(image, mean=0, std=20):#20 oranda gürültülü olur. Ortalama değer, gürültünün merkezi.
    row, col, ch = image.shape #Görüntünün satır (row), sütun (col) ve kanal (ch) sayısını alır.
    gauss = np.random.normal(mean, std, (row, col, ch)).astype(np.float32)
    noisy = image.astype(np.float32) + gauss #Üstte oluşturulan Gaussian gürültü ile piksel piksel toplanır.
    noisy = np.clip(noisy, 0, 255).astype(np.uint8) #Piksel değerlerini 0 ile 255 arasına sıkıştırır.
    return noisy

# Gürültülü Görüntüler
sp_noisy = salt_pepper_noise(image_rgb, oran=0.02)
gauss_noisy = gaussian_noise(image_rgb, std=25)

sp_gaussian_blur = cv2.GaussianBlur(sp_noisy, (5, 5), 0) #5 kernel oluşturulır, görüntü üzerinde her pikselin etrafındaki komşular bu kernel ile çarpılıp toplanır(gaussian dağılımına göre)
sp_median_blur = cv2.medianBlur(sp_noisy, 5) #5 kernel oluşturulur. Her piksel değerinin komşu piksellerinin medyan değeriyle değiştirir.

gauss_gaussian_blur = cv2.GaussianBlur(gauss_noisy, (5, 5), 0)
gauss_median_blur = cv2.medianBlur(gauss_noisy, 5)


#Sonucu görme
plt.figure(figsize=(18, 10))

plt.subplot(3, 3, 1)
plt.imshow(image_rgb)
plt.title("Orijinal")
plt.axis('off')

plt.subplot(3, 3, 2)
plt.imshow(sp_noisy)
plt.title("Salt & Pepper Gürültü")
plt.axis('off')

plt.subplot(3, 3, 3)
plt.imshow(gauss_noisy)
plt.title("Gaussian Gürültü")
plt.axis('off')

plt.subplot(3, 3, 4)
plt.imshow(sp_gaussian_blur)
plt.title("S&P → Gaussian Blur")
plt.axis('off')

plt.subplot(3, 3, 5)
plt.imshow(sp_median_blur)
plt.title("S&P → Median Blur")
plt.axis('off')

plt.subplot(3, 3, 6)
plt.imshow(gauss_gaussian_blur)
plt.title("Gaussian → Gaussian Blur")
plt.axis('off')

plt.subplot(3, 3, 7)
plt.imshow(gauss_median_blur)
plt.title("Gaussian → Median Blur")
plt.axis('off')

plt.tight_layout()
plt.show()