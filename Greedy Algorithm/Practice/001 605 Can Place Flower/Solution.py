from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        result=0
        if len(flowerbed)==1:
            if flowerbed[0]==0:
                result=1
                return self.checkResult(result, n)
            else:
                result=0
                return self.checkResult(result, n)
        if flowerbed[0]==0 and flowerbed[1]==0:
            result+=1
            flowerbed[0]=1
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]!=1:
                result+=1
                flowerbed[i]=1
        if flowerbed[len(flowerbed)-1]==0 and flowerbed[len(flowerbed)-2]==0:
            result+=1
        if result >= n:
            return True
        else:
            return False

    def checkResult(self,result,n):
        if result>=n:
            return True
        else:
            return False