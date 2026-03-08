from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre_sum={}
        pre_sum[0]=1
        ans=0
        cur_sum=0
        for i, num in enumerate(nums):
            cur_sum+=num
            if cur_sum not in pre_sum:
                pre_sum[cur_sum]=0

            target=cur_sum-k
            if target in pre_sum:
                ans+=pre_sum[target]
            pre_sum[cur_sum] += 1

        return ans

def main():
    nums = [1,2,1,2,1]
    k = 3
    print(Solution().subarraySum(nums, k))

if __name__ == "__main__":
    main()