class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        left=0
        hashmap={}
        for right, char in enumerate(s):
            if char in hashmap and hashmap[char]>=left:
                left=hashmap[char]+1
            hashmap[char]=right
            ans=max(ans, right-left+1)
        return ans


def main():
    s="abba"
    print(Solution().lengthOfLongestSubstring(s))

if __name__ == "__main__":
    main()