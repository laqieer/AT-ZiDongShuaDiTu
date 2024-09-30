# 一定要先装好轮子哦
#                   -- 作者：mihu

import cv2                              # pip install opencv-python
import numpy                            # pip install numpy
from PIL import ImageGrab               # pip install pillow
import mouse                            # pip install mouse
import sys, time, ctypes                # python自带 不用安装
from random import random               # python自带 不用安装

img_tap_next = cv2.imread('tap_next.png' ) #加载模板图片
img_tap_next_x =  2278
img_tap_next_y =  1497
img_tap_next_w =  266
img_tap_next_h =  56

img_once_again = cv2.imread('once_again.png' ) #加载模板图片
img_once_again_x =  1402
img_once_again_y =  1453
img_once_again_w =  421
img_once_again_h =  75

THRESHOLD = 0.7

def clickTapNext():
    #截图
    img_src = ImageGrab.grab( bbox=(img_tap_next_x, img_tap_next_y, img_tap_next_x + img_tap_next_w, img_tap_next_y + img_tap_next_h) ) # x1, y1, x2, y2
    # img_src.save("capture.jpg") # for debug
    img_src = cv2.cvtColor(numpy.asarray(img_src), cv2.COLOR_RGB2BGR)

    #模板匹配
    result = cv2.matchTemplate(img_src, img_tap_next, cv2.TM_CCOEFF_NORMED)
    min_max = cv2.minMaxLoc(result)  #计算匹配度
    print('result.min_max:', min_max)

    # 如果匹配度很高，则认为找到Tap Next，于是模拟鼠标单击
    if min_max[1] > THRESHOLD :
        print('找到Tap Next，模拟鼠标单击')
        mouse.move(str(int((img_tap_next_x + img_tap_next_w * random()) / 2)), str(int((img_tap_next_y + img_tap_next_h * random()) / 2)))
        mouse.click()

def clickOnceAgain():
    #截图
    img_src = ImageGrab.grab( bbox=(img_once_again_x, img_once_again_y, img_once_again_x + img_once_again_w, img_once_again_y + img_once_again_h) ) # x1, y1, x2, y2
    # img_src.save("capture.jpg") # for debug
    img_src = cv2.cvtColor(numpy.asarray(img_src), cv2.COLOR_RGB2BGR)

    #模板匹配
    result = cv2.matchTemplate(img_src, img_once_again, cv2.TM_CCOEFF_NORMED)
    min_max = cv2.minMaxLoc(result)  #计算匹配度
    print('result.min_max:', min_max)

    # 如果匹配度很高，则认为找到再出击，于是模拟鼠标单击
    if min_max[1] > THRESHOLD :
        print('找到再出击，模拟鼠标单击')
        mouse.move(str(int((img_once_again_x + img_once_again_w * random()) / 2)), str(int((img_once_again_y + img_once_again_h * random()) / 2)))
        mouse.click()

if __name__ == '__main__':
    # 判断当前进程是否以管理员权限运行
    if ctypes.windll.shell32.IsUserAnAdmin() :
        print('当前已是管理员权限')
        while True:
            clickTapNext()
            clickOnceAgain()
            time.sleep(3 + 2 * random())
    else:
        print('当前不是管理员权限，以管理员权限启动新进程...')
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
