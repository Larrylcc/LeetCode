from typing import List

class Solution:
    def answerArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        answer=0
        while left<right:
            y=min(height[left],height[right])
            x=right-left
            area=x*y
            if answer<area:
                answer=area
            if y==height[left]:
                left+=1
            else:
                right-=1
        return answer