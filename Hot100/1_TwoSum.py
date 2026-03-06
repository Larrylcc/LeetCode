from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for index, num in enumerate(nums):
            diff = target-num
            if diff in hash_map:
                return [index, hash_map[diff]]
            hash_map[num]=index
        return []
