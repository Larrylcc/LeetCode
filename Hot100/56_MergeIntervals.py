from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0]))
        ans=[]
        temp=[-1,-1]
        for val in intervals:
            cur=[val[0], val[1]]
            if temp[1]<cur[0]:#开启新temp
                #先把原temp存到最终答案里
                if temp[0]!=-1:
                    ans.append(temp)
                temp=cur
            elif temp[1]>=cur[0]:
                temp[1]=max(temp[1], cur[1])
        ans.append(temp)
        return ans