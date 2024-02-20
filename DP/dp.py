class Solution:
    def jump(self, nums:[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step
    
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 3, 1, 1, 4]
    print(solution.jump(nums))  # 应该输出最少跳跃次数，对于这个例子是 2