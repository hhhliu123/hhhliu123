import pyautogui
import cv2
import numpy as np
# 截取屏幕
screenshot = pyautogui.screenshot()

# 将屏幕截图转换为OpenCV格式
screen = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# 加载要搜索的图像
template = cv2.imread('template_image.png', 0)

# 图像匹配
res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# 如果匹配度足够高，则移动鼠标
if max_val > 0.8:
    pyautogui.moveTo(max_loc[0], max_loc[1])
