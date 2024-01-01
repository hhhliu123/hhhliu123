import pyautogui
import cv2
# screenshot = pyautogui.screenshot()
# screenshot.save('screen.png')  # 保存屏幕截图以用于后续处理
screen_path = 'F:\py\game\image\screen.jpg'
template_path = 'F:\py\game\image\image.jpg'
template = cv2.imread(template_path)  # 读取模板图像
screen = cv2.imread(screen_path)  # 读取屏幕截图
result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# 选取最佳匹配位置
# top_left = max_loc
# w, h = template.shape[::-1]
# center_point = (top_left[0] + w // 2, top_left[1] + h // 2)
# 先移动鼠标到指定位置，然后点击
if max_val > 0.8:
    pyautogui.moveTo(max_loc)
# pyautogui.moveTo(top_left)
# pyautogui.click()
