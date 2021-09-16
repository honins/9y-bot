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
from src.config import env

# 半屏团练
# location = pyautogui.locateOnScreen(image='../static/right.png', region=(260, 750, 700, 50), confidence=0.9)
# location = pyautogui.locateOnScreen(image='../static/down.png', region=(260, 750, 700, 50), confidence=0.9)

# 测试

if env == 'test':
    image_path = []
    image_path.append("../static/half/up.png")
    image_path.append("../static/half/down.png")
    image_path.append("../static/half/K.png")

if env == 'prod':
    image_path = []
    image_path.append("../static/prod/up.png")
    image_path.append("../static/prod/down.png")
    image_path.append("../static/prod/left.png")
    image_path.append("../static/prod/right.png")
    image_path.append("../static/prod/J.png")
    image_path.append("../static/prod/K.png")

while True:

    locations = found_location(image_path)

    # TODO 根据list中的dict的left排序
    locations.sort(key=lambda k: k.get('location', 0))

    time.sleep(0.5)

    for location in locations:
        do_action(location.get('key'), location.get('location'))
