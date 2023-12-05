class Solution:
    def __init__(self):
        self.memo = {}
    
    def get_max_profit(self, profit:list, weight:list, capacity:int) -> int:
        return self.max_profit_helper(0, profit, weight, capacity)
    
    def max_profit_helper(self, index:int, profit:list, weight:list, capacity:int) -> int:
        if index >= len(weight):
            return 0
        if (index, capacity) in self.memo:
            return self.memo[(index, capacity)]
        # profit by skipping current weight
        self.memo[(index, capacity)] = self.max_profit_helper(index+1, profit, weight, capacity)
        # profit by considering the current weight
        new_cap = capacity - weight[index]
        if new_cap >= 0:
            p = profit[index] + self.max_profit_helper(index, profit, weight, new_cap)
            self.memo[(index, capacity)] = max(p, self.memo[(index, capacity)])
        return self.memo[(index, capacity)]
    
if __name__ == "__main__":
    sol = Solution()
    profit = [4,4,7,1]
    weight = [5,2,3,1]
    print(sol.get_max_profit(profit,weight,8))