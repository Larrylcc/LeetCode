from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1=set(nums)
        count=1
        answer=0
        for num in set1:
            if num-1 not in set1:
                while num+1 in set1:
                    count+=1
                    num+=1
            if count>answer:
                answer=count
            count=1
        return answer