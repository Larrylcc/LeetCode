from collections import Counter
from typing import List
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = Counter(t)
        count=0
        min_l, min_length=None,None
        l=0
        for i in range(len(s)):
            if s[i] not in freq:
                continue
            freq[s[i]]-=1
            if freq[s[i]]>=0:
                count+=1
            while count == len(t):
                #初始化
                if min_length == None or i-l+1<min_length:
                    min_l=l
                    min_length=i-l+1
                if s[l] in freq:
                    freq[s[l]]+=1
                    if freq[s[l]]>0:
                        count-=1
                l+=1
        return "" if min_length is None else s[min_l:min_l+min_length]