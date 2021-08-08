# 9y-bot

## 团练

基本思路：

思路一
- 找到按键的矩形坐标范围
- 切割范围内的图片成为一个个字母按键（不确定是否需要先将坐标范围内的内容截图，存到本地，然后对本地图片进行识别）
- 使用图像文字识别库（比如baidu_aip），解析成一个个按键操作
- 使用自动化输入工具（例如pyautogui），按序输入按键。

思路二
- 获得所有按键的图片素材
- 使用pyautogui获取各个按键出现的坐标，得到坐标数组
- 将坐标数组按x轴重小到大排列，使用pyautogui依次键入

总体来看思路二更加简单，也同样有效。

参考文档：https://www.cnblogs.com/ffrs/p/11353650.html