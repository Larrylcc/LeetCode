from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        count = 1
        ans = 0
        for num in nums:
            if num - 1 not in set_nums:
                count = 1
                current_num = num
                while current_num + 1 in set_nums:
                    count += 1
                    current_num += 1
                if ans < count:
                    ans = count

        return ans
