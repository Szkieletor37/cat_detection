# OpenCV2の読み込み
import cv2
# フォルダ内のファイルの一覧を取得するglobモジュール
import glob
# ディレクトリを移動できるosモジュール
import os

imageFilePaths = glob.glob("./cats/**/*.jpg")

for imageFilePath in imageFilePaths:
    annotationFilePath = imageFilePath + ".cat"
    directoryOfImageFile = imageFilePath.split("/")[2]

    # 画像を取得
    img = cv2.imread(imageFilePath)

    with open(annotationFilePath) as f:

        # 文字列の読み込み
        # ファイルは先頭に点の数、それから9個の(x,y)の組
        spritedStringFromFile = f.read().split()

        # リストの各要素を文字列から整数に変換したリストを作る
        numbersFromFile = list(map(int, spritedStringFromFile))

        # x座標とy座標の最大値、最小値を求める
        max_x = max(numbersFromFile[1::2])
        min_x = min(numbersFromFile[1::2])
        max_y = max(numbersFromFile[2::2])
        min_y = min(numbersFromFile[2::2])

        # トリミングする正方形の幅を決める
        # max - min をして、大きい方を採用
        # 余白を持たせる

        margin = 30

        if (max_x - min_x) > (max_y - min_y):
            widthOfTrimmedSquare = (max_x - min_x) + margin
        else:
            widthOfTrimmedSquare = (max_y - min_y) + margin

        # 整数除算
        x = min_x - margin // 2
        y = min_y - margin // 2

    if x < 0 or y < 0:
        print("skip!")
        continue

    if y + widthOfTrimmedSquare + margin > img.shape[0] or x + widthOfTrimmedSquare + margin > img.shape[1]:
        print("skip!")
        continue

    print(str(x) + " " + str(y) + " " + str(widthOfTrimmedSquare))

    face_cut = img[y:y+widthOfTrimmedSquare, x:x+widthOfTrimmedSquare]

    imageFileID = os.path.splitext(os.path.basename(imageFilePath))[0]

    dirname = "./cats_face_cut/" + directoryOfImageFile

    if not os.path.exists(dirname):
        os.mkdir(dirname)

    cv2.imwrite(os.path.join(dirname, imageFileID + '_face_cut.jpg'), face_cut)
