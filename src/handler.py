import pyautogui


def found_location(image_path):
    # location = pyautogui.locateOnScreen(image=image_path, region=(370, 640, 580, 30), confidence=0.9)
    locations_gene = pyautogui.locateAllOnScreen(image=image_path, region=(370, 640, 580, 30), confidence=0.9)

    locations = []

    temp_dir = {}

    # 输出坐标
    for location in locations_gene:
        locations.append(location)

    return locations


def do_action(a_location: object) -> object:
    if a_location:
        # 利用center()函数获取目标图像在系统中的中心坐标位置
        x, y = pyautogui.center(a_location)
        print('center()', x, y)

        # 对识别出的目标图像进行点击
        # 参数x,y代表坐标位置，clicks代表点击次数,button可以设置为左键或者右键
        pyautogui.click(x=x, y=y, clicks=1, button='right')
        print("do click!")

        pyautogui.press('d')

        pyautogui.write("d")
        # print("press right!")

    else:
        print("None!")

    return True
