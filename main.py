#important!: please read readme.md first when you study this project
# 先读readme.md
#开始进入正题。已经挑选了一些图片 首先做人脸识别检测图片质量，建议选择单纯背景色+单人的图片
import cv2
# 加载特征数据
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# 读取图片
im = cv2.imread('grey.jpg')
# 检测人脸，返回人脸的位置信息
faces = face_detector.detectMultiScale(im)
# 遍历人脸
for x, y, w, h in faces:
    # 在人脸区域绘制矩形
    cv2.rectangle(im, (x, y), (x+w, y+h), (255, 255, 0), 2)
# 显示图像
cv2.imshow('im', im)
cv2.waitKey(0)
cv2.destroyAllWindows()