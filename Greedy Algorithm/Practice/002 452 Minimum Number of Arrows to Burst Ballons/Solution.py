from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda item:item[1])
        result=1
        temp=points[0][1]
        for i in range(len(points)):
            if points[i][0]>temp:
                temp=points[i][1]
                result+=1

        return result