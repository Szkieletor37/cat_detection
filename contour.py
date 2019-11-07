import cv2
import numpy as np
import glob

imageFilePaths = glob.glob("./cats_face_cut/**/*.jpg")

# あとでfor文に変える
imageFilePath = imageFilePaths[0]

# 画像の読み込み
img = cv2.imread(imageFilePath)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# H,S,Vにsplit
h_img, s_img, v_img = cv2.split(hsv)
s_img = cv2.bitwise_not(s_img)

cv2.imwrite("s_img.jpg", s_img)

# ヒストグラムの平坦化
hist_s_img = cv2.equalizeHist(s_img)

# 二値化
_, result_bin = cv2.threshold(s_img, 200, 255, cv2.THRESH_BINARY)

cv2.imwrite("result_bin.jpg", result_bin)
