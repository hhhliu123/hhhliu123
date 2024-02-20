import time
import pyautogui
import cv2
import numpy as np


# 定义需要检测的图像

cg40 = cv2.imread('F:\py\game\image\challenge40.png')
startcg = cv2.imread('F:\py\game\image\startchallenge.png')
auto = cv2.imread('F:\py\game\image\Auto.png')
btend = cv2.imread('F:\py\game\image\Batteend.png')

# 定义点击坐标
cgclick = (2251,1456)
stclick = (2137,1457)
atclick = (2347,61)
btclick = (1614,1424)

# 设置匹配阈值（可以根据需要调整）
threshold = 0.8


while True:
   # 截取桌面截图
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    # 在桌面截图中寻找匹配
    recg40 = cv2.matchTemplate(screenshot, cg40, cv2.TM_CCOEFF_NORMED)
    restartcg = cv2.matchTemplate(screenshot, startcg, cv2.TM_CCOEFF_NORMED)
    reauto = cv2.matchTemplate(screenshot, auto, cv2.TM_CCOEFF_NORMED)
    rebtend = cv2.matchTemplate(screenshot, btend, cv2.TM_CCOEFF_NORMED)

    # 检查是否有匹配的图像
    if np.max(recg40) > threshold:
        # 执行相应的操作
        pyautogui.moveTo(cgclick)
        pyautogui.click()

    if np.max(restartcg) > threshold:
        # 执行相应的操作
        pyautogui.click(stclick)

    if np.max(reauto) > threshold:
        # 执行与 image3 匹配的操作
        print("检测到图像3")
        # 执行相应的操作
        pyautogui.click(atclick)

    if np.max(rebtend) > threshold:
        # 执行与 image4 匹配的操作
        print("检测到图像4")
        pyautogui.click(btclick)

    # 可以加入适当的延迟，以控制检测频率
    time.sleep(0.5)
