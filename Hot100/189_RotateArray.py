from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        new=[0]*n
        for i,num in enumerate(nums):
            new[(i+k)%n]=num
        nums[:]=new

def main():
    nums=[1,2,3,4,5,6,7]
    k=3
    Solution().rotate(nums,k)
    print(nums)

if __name__ == "__main__":
    main()