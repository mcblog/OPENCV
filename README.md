opencv是一个基于BSD许可发行（也就是俗称的开源）的跨平台计算机视觉库，可以运行在Linux、Windows、Android和Mac OS上。
由一系列 C 函数和少量 C++ 类构成的它轻量且高效，并提供了Python、Ruby、MATLAB等语言的接口，实现了图像处理和计算机视觉方面的很多通用算法。
——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
对于python而言，在引用opencv库的时候需要写为import cv2。其中，cv2是opencv的C++命名空间名称，使用它来表示调用的是C++开发的opencv的接口。
准备工作：
    创建python project
    使用前安装opencv这两个库：
    ‘pip install opencv-python‘ opencv主要模块
    ‘pip install opencv-contrib-python’  除了主要模块还有扩展模块。
    cv2库的相关info：https://www.cnblogs.com/silence-cho/p/10926248.html
    下载opencv source：https://github.com/opencv/opencv/archive/4.2.0.zip
    解压并找到’haarcascade_frontalface_default.xml‘ 这是个默认的人脸识别
    导入