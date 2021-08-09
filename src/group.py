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

count = 0

while True:

    count = count + 1

    print(count)

    location = pyautogui.locateOnScreen(image='../static/up.png')

    # 输出坐标
    print(location)

    if location:
        # 利用center()函数获取目标图像在系统中的中心坐标位置
        x, y = pyautogui.center(location)
        print('center()', x, y)

        # 对识别出的目标图像进行点击
        # 参数x,y代表坐标位置，clicks代表点击次数,button可以设置为左键或者右键
        pyautogui.click(x=x, y=y, clicks=1, button='left')

        print("do click!")

    else:
        print("None!")
