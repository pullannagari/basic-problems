class Solution:
    def __init__(self) -> None:
        self.memo = {}
    
    def get_max_profit(self, weights: list, profits:list, capacity:int) -> int:
        return self.max_profit_calc(0, weights, profits, capacity)
    
    def max_profit_calc(self, index, weights:list, profits:list, rem_cap:int) -> int:
        if index >= len(profits):
            return 0
        if (index, rem_cap) in self.memo:
            return self.memo[(index, rem_cap)]
        max_profit = self.max_profit_calc(index+1, weights, profits, rem_cap)
        self.memo[(index+1, rem_cap)] = max_profit
        if rem_cap - weights[index] >= 0:
            profit = profits[index] + self.max_profit_calc(index+1, weights, profits, rem_cap-weights[index])
            max_profit = max(max_profit, profit)
        self.memo[(index, rem_cap)] = max_profit
        return max_profit       
    
if __name__ == "__main__":
    sol = Solution()
    profits = [4, 4, 7, 1, 3, 6, 8]
    weights = [5, 2, 3, 1, 2, 1, 4]
    capacity = 8
    print(sol.get_max_profit(weights, profits, capacity))