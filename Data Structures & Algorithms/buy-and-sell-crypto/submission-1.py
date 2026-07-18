class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxp = 0
        while r < len(prices) :
            if prices[r] > prices[l]:
                pro = prices[r] - prices[l]
                maxp = max(pro,maxp)
            else:
                l = r
            r += 1
        return maxp




        