import pyautogui
import time

# 判定目标截图在系统上的位置

# location = []
#
# location1 = [pyautogui.locateAllOnScreen(image='../static/down-min.png')]
# location1 = [pyautogui.locateAllOnScreen(image='../static/down-min.png')]
# location2 = [pyautogui.locateAllOnScreen(image='../static/down-min.png')]
#
# location.append(location1)
# location.append(location2)

# 测试
# 250 500 - 700 500
# 250 550 - 700 550
#
# 真实团练
# 740 750 - 1190 750
#
count = 0

while True:

    time.sleep(1)

    count = count + 1

    print(count)

    # 视频测试
    # location = pyautogui.locateOnScreen(image='../static/up.png', region=(250, 500, 450, 50), confidence=0.9)

    # 真实团练
    # location = pyautogui.locateOnScreen(image='../static/right.png', region=(740, 750, 450, 50), confidence=0.9)

    # 半屏团练
    # location = pyautogui.locateOnScreen(image='../static/right.png', region=(260, 750, 700, 50), confidence=0.9)
    # location = pyautogui.locateOnScreen(image='../static/tmp.png', region=(260, 750, 700, 50), confidence=0.9)

    # 测试名字
    location = pyautogui.locateOnScreen(image='../static/tmp.png', confidence=0.9)

    # 输出坐标
    print(location)

    if location:
        # 利用center()函数获取目标图像在系统中的中心坐标位置
        x, y = pyautogui.center(location)
        print('center()', x, y)

        # 对识别出的目标图像进行点击
        # 参数x,y代表坐标位置，clicks代表点击次数,button可以设置为左键或者右键
        pyautogui.click(x=x, y=y, clicks=2, button='left')
        print("do click!")

        pyautogui.press('d')

        pyautogui.write("d")
        # print("press right!")

    else:
        print("None!")