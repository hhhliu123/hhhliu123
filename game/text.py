import time
# import pyautogui
import cv2
import numpy as np
import pydirectinput

# pyautogui.moveTo(1948, 1172)
# time.sleep(1)
pydirectinput.click()
# time.sleep(4)
# pyautogui.click()

import numpy as np
import matplotlib.pyplot as plt

# 模拟的温度控制系统
class TemperatureSystem:
    def __init__(self):
        self.temperature = 0  # 初始温度

    def update_temperature(self, heat_power):
        # 更新温度，简化的物理模型
        self.temperature += 0.1 * (heat_power - (self.temperature - 20) / 10)

# 单神经元PID控制器
class SingleNeuronPID:
    def __init__(self):
        # 初始化权重（对应于PID的P、I、D参数）
        self.weights = np.random.rand(3)

    def update_weights(self, error, previous_errors):
        # 使用简单的梯度下降来更新权重
        learning_rate = 0.01
        gradient = np.array([error, sum(previous_errors), error - previous_errors[-1]])
        self.weights -= learning_rate * gradient

    def control_signal(self, error, previous_errors):
        # 生成控制信号
        return np.dot(self.weights, np.array([error, sum(previous_errors), error - previous_errors[-1]]))

# 初始化
system = TemperatureSystem()
controller = SingleNeuronPID()
target_temperature = 200
errors = []

# 模拟过程
for step in range(100):
    current_temperature = system.temperature
    error = target_temperature - current_temperature
    errors.append(error)

    if len(errors) > 5:
        errors.pop(0)

    # 更新权重
    controller.update_weights(error, errors)

    # 生成控制信号
    heat_power = controller.control_signal(error, errors)

    # 更新系统温度
    system.update_temperature(heat_power)

    # 打印和绘图
    print(f"Step {step}, Temperature: {current_temperature}, Control: {heat_power}")
    plt.plot(step, current_temperature, 'bo')

# 结果展示
plt.axhline(y=target_temperature, color='r', linestyle='-')
plt.title("Temperature vs. Time")
plt.xlabel("Time Step")
plt.ylabel("Temperature")
plt.show()
