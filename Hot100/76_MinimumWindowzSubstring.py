from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_count=Counter(t)
        min_l=None
        min_length=None
        l=0
        count=0
        for i, char in enumerate(s):
            if char not in char_count:
                continue
            if s[i] in char_count:
                char_count[s[i]]-=1
            if char_count[s[i]]>=0:
                count+=1
            while count==len(t):
                if min_length is None or min_length > i-l+1:
                    min_l=l
                    min_length=i-l+1
                if s[l] in char_count:
                    char_count[s[l]]+=1
                    if char_count[s[l]]>0:
                        count-=1
                l+=1
        return "" if min_length is None else s[min_l:min_l+min_length]