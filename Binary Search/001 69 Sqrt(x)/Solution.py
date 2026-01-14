class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=1,x
        while l<=r:
            mid=(l+r)//2
            x_square=mid*mid
            if x_square==x:
                return mid
            if x_square>x:
                r=mid-1
            else:
                l=mid+1
        return r