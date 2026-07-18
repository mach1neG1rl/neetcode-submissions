class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0

        for i in range(len(prices)):
            if lowest > prices[i]:
                lowest = prices[i]
            elif prices[i] - lowest > profit:
                profit = prices[i] - lowest
        
        return profit