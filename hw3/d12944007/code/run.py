'''
姓名: 楊德倫 (Te-Lun Yang)
學號: D12944007

安裝套件
$ pip install opencv-python matplotlib

執行流程
$ cd d12944007
$ python code/run.py
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 建立 histogram equalization 函式，將圖片連行轉換
def get_histogram_equalization_img(img):
    # 計算 historgram
    hist, bins = np.histogram(img.flatten(), 256, [0,256])
    
    # 計算 CDF
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    
    # 建立 mask
    mask = cdf > 0
    
    # 將 CDF 正規化 (Normalization)
    cdf_normalized = (cdf - cdf[mask].min()) * 255 / (cdf[-1] - cdf[mask].min())
    
    # 將原始照片(拍拍照)對應到 equalize 之後的值
    img_equalized = cdf_normalized[img]
    
    # 回傳 equalize 之後的圖片物件
    return img_equalized

# 以灰階模式 (IMREAD_GRAYSCALE) 來讀取圖片
selfie = cv2.imread('origin.png', cv2.IMREAD_GRAYSCALE)

# Apply histogram equalization
selfie_equalized = get_histogram_equalization_img(selfie)

# 繪製圖片 (以 2x2 格式呈現，將 4 張圖片整合在同一張)
plt.figure(figsize=(12, 6))

# 原始自拍照 (灰階)，放在圖片左上角
plt.subplot(2, 2, 1)
plt.imshow(selfie, cmap='gray')
plt.title('Original Selfie')
plt.axis('off')

# 原始自拍照的 histogram，放在圖片右上角
plt.subplot(2, 2, 2)
plt.hist(selfie.ravel(), 256, [0,256])
plt.title('Original Histogram')

# Equalize 自拍照之後的照片，放在圖片右下角
plt.subplot(2, 2, 3)
plt.imshow(selfie_equalized, cmap='gray')
plt.title('Equalized Selfie')
plt.axis('off')

# Equalize 自拍照之後的 histogram，放在圖片右下角
plt.subplot(2, 2, 4)
plt.hist(selfie_equalized.ravel(), 256, [0,256])
plt.title('Equalized Histogram')

# 儲存結果 (chart) 在作業指定位置
plt.savefig("result/result.png", dpi=300, format='png', bbox_inches='tight')

# 輸出圖片
plt.show()