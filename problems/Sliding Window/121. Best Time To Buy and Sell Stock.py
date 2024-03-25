# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Time O(n) | Space O(1)
# If the next price is less than the current price, that means that price is the best price. Update the left pointer
# If the next price is greater than the current price, that means that price is the best price. Update the right pointer

def max_profit(prices):
    left = 0
    right = 1
    max_profit = 0

    while right < len(prices):
        current_profit = prices[right] - prices[left]

        if current_profit > max_profit:
            max_profit = current_profit

        if prices[left] > prices[right]:
            left = right
        right += 1

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))
