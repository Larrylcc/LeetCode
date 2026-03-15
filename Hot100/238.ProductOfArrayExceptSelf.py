from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            if i == 0:
                ans[i] = 1
                continue
            ans[i] = ans[i - 1] * nums[i - 1]
        suf = 1
        for i in range(n - 1, -1, -1):
            ans[i] = ans[i] * suf
            suf *= nums[i]
        return ans