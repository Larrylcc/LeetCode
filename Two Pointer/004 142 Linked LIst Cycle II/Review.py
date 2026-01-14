from collections import Counter
from typing import List
class Review:
    def minWindow(self, s: str, t: str) -> str:
        min_l, min_length = None, None
        count=0
        dict=Counter(t)
        l=0
        for i in range(len(s)):
            if s[i] not in dict:
                continue
            dict[s[i]] -= 1
            if dict[s[i]]>=0:
                count += 1
            while count==len(t):
                if min_length==None or i-l+1<min_length:
                    min_l=l
                    min_length=i-l+1
                if s[l] in dict:
                    dict[s[l]]+=1
                    if dict[s[l]]>0:
                        count-=1
                l+=1

        return "" if min_length is None else s[min_l:min_l+min_length]