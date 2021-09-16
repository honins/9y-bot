import pyautogui
import time

from src.config import env


def found_location(image_path):
    locations = []

    for path in image_path:
        if env == 'test':
            scan_location = pyautogui.locateAllOnScreen(image=path, region=(390, 600, 180, 30), confidence=0.9)

        if env == 'prod':
            scan_location = pyautogui.locateAllOnScreen(image=path, region=(800, 750, 300, 50), confidence=0.9)

        # 输出坐标djj
        for location in scan_location:
            temp_dir = {}
            if 'up' in path:
                temp_dir['key'] = 'w'

            if 'down' in path:
                temp_dir['key'] = 's'

            if 'left' in path:
                temp_dir['key'] = 'a'

            if 'right' in path:
                temp_dir['key'] = 'd'

            if 'J' in path:
                temp_dir['key'] = 'j'

            if 'K' in path:
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
        print('pyautogui.write', key)

        pyautogui.write(key, interval=0.1)

    else:
        print("None!")

    return True
