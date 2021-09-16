import pyautogui
import time


def found_location(image_path):
    # location = pyautogui.locateOnScreen(image=image_path, region=(370, 640, 580, 30), confidence=0.9)

    locations = []

    for path in image_path:
        locations_gene = pyautogui.locateAllOnScreen(image=path, region=(390, 600, 180, 30), confidence=0.9)
        # 输出坐标
        for location in locations_gene:
            temp_dir = {}
            if 'up' in path:
                temp_dir['key'] = 'w'

            if 'down' in path:
                temp_dir['key'] = 's'

            if 'left' in path:
                temp_dir['key'] = 'a'

            if 'right' in path:
                temp_dir['key'] = 'd'

            if 'j' in path:
                temp_dir['key'] = 'j'

            if 'k' in path:
                temp_dir['key'] = 'k'

            temp_dir['location'] = location
            locations.append(temp_dir)

    return locations


def do_action(key, a_location):
    if a_location:
        # 利用center()函数获取目标图像在系统中的中心坐标位置
        x, y = pyautogui.center(a_location)
        print('center()', x, y)

        # 对识别出的目标图像进行点击
        # 参数x,y代表坐标位置，clicks代表点击次数,button可以设置为左键或者右键
        pyautogui.click(x=x, y=y, clicks=1, button='right')
        print(time.time(), "do click!")

        pyautogui.write(key)

        print('pyautogui.write', key)

    else:
        print("None!")

    return True
