import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

def plot_covariance_ellipse(data):
    """
    绘制给定数据的协方差椭圆。
    
    :param data: 二维数据集，形状为 (n_samples, 2)
    """
    # 计算数据的均值和协方差矩阵
    mean = np.mean(data, axis=0)
    cov = np.cov(data, rowvar=False)

    # 计算协方差矩阵的特征值和特征向量
    eigenvalues, eigenvectors = np.linalg.eigh(cov)

    # 计算椭圆的宽度和高度（特征值的平方根）
    width, height = 2 * np.sqrt(eigenvalues)

    # 计算椭圆的旋转角度
    angle = np.arctan2(*eigenvectors[:,0][::-1])

    # 创建并绘制椭圆
    ellipse = Ellipse(xy=mean, width=width, height=height, angle=np.degrees(angle), edgecolor='r', fc='None')
    fig, ax = plt.subplots()
    ax.add_patch(ellipse)
    ax.scatter(data[:,0], data[:,1], s=5)  # 绘制原始数据点

    # 设置图形的边界
    plt.xlim(mean[0] - width, mean[0] + width)
    plt.ylim(mean[1] - height, mean[1] + height)
    plt.show()

# 示例数据
data = np.random.multivariate_normal([2, 3], [[1, 0.5], [0.5, 1]], size=1000)

# 绘制协方差椭圆
plot_covariance_ellipse(data)
