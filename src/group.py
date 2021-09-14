import pyautogui
import time

# 测试坐标
# 250 500 - 700 500
# 250 550 - 700 550
#
# 真实团练坐标
# 740 750 - 1190 750
#

from src.handler import found_location
from src.handler import do_action

# 真实团练
# location = pyautogui.locateOnScreen(image='../static/right.png', region=(740, 750, 450, 50), confidence=0.9)

# 半屏团练
# location = pyautogui.locateOnScreen(image='../static/right.png', region=(260, 750, 700, 50), confidence=0.9)
# location = pyautogui.locateOnScreen(image='../static/down.png', region=(260, 750, 700, 50), confidence=0.9)

# 测试

env = 'test'

if env == 'test':
    image_path = []
    image_path.append("../static/half/up.png")
    image_path.append("../static/half/down.png")
    image_path.append("../static/half/k.png")

if env == 'prod':
    image_path = []
    image_path.append("../static/down.png")
    image_path.append("../static/up.png")
    image_path.append("../static/k.png")

# image_path = "../static/half/up.png"
while True:


    locations = found_location(image_path)

    # TODO 根据list中的dict的left排序
    locations.sort(key= lambda x:x.items())

    time.sleep(3)

    for location in locations:
        for (key, sorted_location) in location.items():
            do_action(key, sorted_location)
