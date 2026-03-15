from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0]))
        ans = []
        cur = intervals[0]
        for interval in intervals:
            if interval[0] <= cur[1] < interval[1]:
                cur[1] = interval[1]
            elif cur[1] < interval[0]:
                ans.append(cur)
                cur = interval
        ans.append(cur)
        return ans