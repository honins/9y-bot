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
# location = pyautogui.locateOnScreen(image='../static/tmp.png', region=(260, 750, 700, 50), confidence=0.9)

# 测试
image_path = "../static/tmp.png"

locations = found_location(image_path)


for location in locations:
    print("---")
    print(location)
    do_action(location)

