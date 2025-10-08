from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        result=0
        for price in prices[1:]:
            if price>start:
                result+=price-start
                start=price
            else:
                start=price
        return result