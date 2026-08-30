class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        min = prices[0]
        for i in prices:
            if i < min:
                min = i
            profit = i - min
            if profit > max_prof:
                max_prof = profit
        return max_prof
        