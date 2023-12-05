class Solution:
    def __init__(self):
        pass
    
    def max_profit(self, profit:list, weight:list, capacity:int) -> int:
        M = capacity + 1
        N = len(weight)
        memo = [[0]*M for _ in range(N)]
        for i in range(N):
            memo[i][0] = 0
        for i in range(M):
            if i < weight[0]:
                memo[0][i] = 0
            else:
                memo[0][i] = profit[0]
        # recurrence relation
        for i in range(1, N):
            for j in range(1, M):
                skip = memo[i-1][j]
                include = 0
                if weight[i] <= j:
                    include = profit[i] + memo[i-1][j-weight[i]]
                memo[i][j] = max(skip, include) 
        print(memo)
        return memo[N-1][M-1]
        
if __name__ == "__main__":
    sol = Solution()
    profits = [4, 4, 7, 1, 3, 6, 8]
    weights = [5, 2, 3, 1, 2, 1, 4]
    capacity = 8
    print(sol.max_profit(profits, weights, capacity))
                
    