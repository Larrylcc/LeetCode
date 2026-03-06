from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=1

    def lowerRange(self, nums:List[int], target:int) -> int:
        l,r=0,len(nums)
        while l<r:
            mid=(l+r)//2
            if nums[mid]<target:
                l=mid+1
            else:
                r=mid
        return l

    def upperRange(self, nums:List[int], target:int) -> int:
        l,r=0,len(nums)
        while l<r:
            mid=(l+r)//2
            if nums[mid]>target:
                r=mid-1
            else:
                l=mid
        return r