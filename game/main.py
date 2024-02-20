import tkinter as tk
import threading
import keyboard
import time
import time
import pyautogui
import cv2
import numpy as np


# 定义需要检测的图像

cg40 = cv2.imread('F:\py\game\image\challenge40.png')
startcg = cv2.imread('F:\py\game\image\startchallenge.png')
auto = cv2.imread('F:\py\game\image\Auto.png')
btend = cv2.imread('F:\py\game\image\batteend.png')

# 定义点击坐标
cgclick = (2251,1456)
stclick = (2137,1457)
atclick = (2347,61)
btclick = (1614,1424)

# 设置匹配阈值（可以根据需要调整）
threshold = 0.8

# 创建一个标志变量，用于控制循环是否继续执行
running = False

def start_button_click():
    global running
    if not running:
        running = True
        start_button.config(text="停止")
        # 启动一个线程执行循环
        threading.Thread(target=run_loop).start()
    else:
        running = False
        start_button.config(text="开始")



# 主要部分
def run_loop():
    global running

    while running:
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
            pyautogui.click(cgclick)

        if np.max(restartcg) > threshold:
        # 执行相应的操作
            pyautogui.click(stclick)

        if np.max(reauto) > threshold:
        # 执行与 image3 匹配的操作
          
        
            pyautogui.click(atclick)

        if np.max(rebtend) > threshold:
        # 执行与 image4 匹配的操作
            
            pyautogui.click(btclick)

    # 可以加入适当的延迟，以控制检测频率
        time.sleep(0.5)
        pass




def exit_program():
    root.quit()

# 创建主窗口
root = tk.Tk()
root.title("循环执行程序")

# 创建开始/停止按钮
start_button = tk.Button(root, text="开始", command=start_button_click)
start_button.pack()

# 创建退出按钮
exit_button = tk.Button(root, text="退出", command=exit_program)
exit_button.pack()

# 创建用于显示数字的标签
display_label = tk.Label(root, text="", font=("Helvetica", 24))
display_label.pack()

# 监听空格键事件
keyboard.on_press_key('space', lambda _: start_button_click())

# 监听Esc键事件
keyboard.on_press_key('esc', lambda _: exit_program())

# 启动主循环
root.mainloop()

