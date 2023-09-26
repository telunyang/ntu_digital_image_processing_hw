'''
姓名: 楊德倫 (Te-Lun Yang)
學號: D12944007

安裝套件
$ pip install opencv-python

執行流程
$ cd d12944007
$ python code/run.py
'''

import cv2
import os

# 建立資料夾 (不存在就新增)
folder_path = "results"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# 縮放函式
def scale_img(file_path, ratio, method):
    # 讀取圖片
    img = cv2.imread(file_path)

    # 計算縮放後的尺寸 (type: tuple)
    new_size = (int(img.shape[1] * ratio), int(img.shape[0] * ratio))

    # 回傳縮放後的圖片
    return cv2.resize(img, new_size, interpolation=method)


# 主程式
if __name__ == "__main__":
    # 縮放大小
    list_ratio = [0.2, 5, 32]

    # 自拍照檔案路徑
    file_path = "origin.jpg"

    # 建立每個縮放的圖片
    for ratio in list_ratio:
        # Bilinear
        print(cv2.INTER_LINEAR)
        resize_bilinear_img = scale_img(file_path, ratio, cv2.INTER_LINEAR)

        # Bicubic
        print(cv2.INTER_CUBIC)
        resize_bicubic_img = scale_img(file_path, ratio, cv2.INTER_CUBIC)
        
        # 儲存圖片
        cv2.imwrite(f"results/bilinear_{ratio}x.jpg", resize_bilinear_img)
        cv2.imwrite(f"results/bicubic_{ratio}x.jpg", resize_bicubic_img)