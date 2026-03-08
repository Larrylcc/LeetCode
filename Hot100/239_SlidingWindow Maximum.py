from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        sorted_queue=deque()#记录的值是数组的下标
        for i, num in enumerate(nums):
            while sorted_queue and nums[sorted_queue[-1]]<num:
                sorted_queue.pop()
            sorted_queue.append(i)
            if sorted_queue[0]<=i-k:
                sorted_queue.popleft()
            if i>=k-1:
                ans.append(nums[sorted_queue[0]])
        return ans