"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


def sliding_window_best_time_to_buy_and_sell_stock(prices):
  max_profit = 0
  for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
      if (prices[j] - prices[i]) > max_profit:
        max_profit = prices[j] - prices[i]
  return max_profit


def sliding_window_best_time_to_buy_and_sell_stock(prices):
  max_profit = 0
  l = 0
  for r in range(1, len(prices)):
    if prices[r] < prices[l]:
      l = r
    profit = prices[r] - prices[l]
    max_profit = profit if profit > max_profit else max_profit
  return max_profit


# test cases
prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]
print(prices1, "Pass" if sliding_window_best_time_to_buy_and_sell_stock(prices1) == 5 else "Fail")
print(prices2, "Pass" if sliding_window_best_time_to_buy_and_sell_stock(prices2) == 0 else "Fail")
