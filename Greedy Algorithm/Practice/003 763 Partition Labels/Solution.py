from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        alpha_dict= {}
        for i,char in enumerate(s):
            alpha_dict[char]=i
        result=[]
        start=0
        end=0
        for i,char in enumerate(s):
            end=max(end,alpha_dict[char])
            if end == i:
                result.append(end-start+1)
                start=i+1
        return result