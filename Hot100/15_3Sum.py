class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans=[]
        n=len(nums)
        for i in range(n-2):
            x=nums[i]
            if i>0 and x==nums[i-1]:
                continue
            if x+ nums[i+1]+nums[i+2]>0:
                break
            if x+nums[n-1]+nums[n-2]<0:
                continue
            j=i+1
            k=n-1
            while j<k:
                s=x+nums[j]+nums[k]
                if s>0:
                    k-=1
                elif s<0:
                    j+=1
                else:
                    ans.append([x, nums[j], nums[k]])
                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    k-=1
                    while k>j and nums[k]==nums[k+1]:
                        k-=1
        return ans