from typing import List
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        for i, num in enumerate(nums[:-1]):
            if num>nums[i+1]:
                if(i>0 and nums[i-1]>nums[i+1]):
                    nums[i+1]=nums[i]
                else:
                    nums[i]=nums[i+1]
                break
        for i, num in enumerate(nums[:-1]):
            if num>nums[i+1]:
                return False
        return True