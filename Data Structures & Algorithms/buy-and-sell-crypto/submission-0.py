class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = prices[0]

        for price in prices[1:]:
            # for sell_price                        
            max_profit = max(max_profit, price-buy_price)
            buy_price = min(buy_price, price)
            # computing the profit before updating the minimum guarantees 
        
        return max_profit
        