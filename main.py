#important!: please read readme.md first when you study this project
# 先读readme.md
#开始进入正题。已经挑选了一些图片 首先做人脸识别检测图片质量，建议选择单纯背景色+单人的图片
import cv2
#首先，测试下图片读取
i = cv2.imread('1.jpg')#读取根路径的’1.jpg‘
#显示i
cv2.imshow('im', i)
cv2.waitKey(0)



