from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        intervals.sort(key=lambda item: item[1])
        bound=intervals[0][1]
        for i in range(1,len(intervals)):
            if bound>intervals[i][0]:
                result+=1
            else:
                bound=intervals[i][1]

        return result