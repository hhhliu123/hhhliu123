nums = [2, 3, 1, 1, 4]
n = len(nums)
maxPos, end, step = 0, 0, 0
for i in range(n - 1):
    if maxPos >= i:
        maxPos = max(maxPos, i + nums[i])
        if i == end:
            end = maxPos
            step += 1
print(step)

# 贪心算法
# 每次跳跃的距离取决于当前位置能跳跃的最大距离
# 时间复杂度：O(n)
# 空间复杂度：O(1)