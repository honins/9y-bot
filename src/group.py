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
image_path = []
image_path.append("../static/half/down.png")
image_path.append("../static/half/up.png")
image_path.append("../static/half/k.png")

# image_path = "../static/half/up.png"

locations = found_location(image_path)

sorted(locations, key=lambda items: items)

for (key, location) in locations.items():
    print('key', key, 'location', location)
    do_action(location)

