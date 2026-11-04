class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_profit = 0
        min_price = prices[0]

        for cur_price in prices: 
            
            if cur_price < min_price: 
                min_price = cur_price
                profit = 0
                continue
            
            profit = cur_price - min_price 
            max_profit = max(profit, max_profit)

        return max_profit

            