from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre_sum=[0]*(len(nums)+1)
        ans=None
        min=0
        for i in range(len(nums)):
            pre_sum[i+1]=pre_sum[i]+nums[i]
            temp = pre_sum[i + 1] - min
            if min>pre_sum[i+1]:
                min = pre_sum[i+1]

            if ans is None or temp>ans:
                ans=temp

        return ans