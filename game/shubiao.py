import pyautogui

# 获取当前鼠标坐标
x, y = pyautogui.position()

# 显示坐标
print(f'鼠标当前位置：({x}, {y})')
