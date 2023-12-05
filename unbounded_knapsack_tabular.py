class Solution:
    def __init__(self) -> None:
        pass
    
    def get_maximum_profit(self, profit:list, weight:list, capacity:int) -> int:
        N = len(weight)
        M = capacity + 1
        dp = [[0]*M for _ in range(N)]
        for i in range(N):
            dp[i][0] = 0
        for i in range(M):
            if i >= weight[0]:
                q = i//weight[0]
                dp[0][i] = q * profit[0]
        for i in range(1, N):
            for c in range(1, M):
                skip_p = dp[i-1][c]
                include = 0
                if c-weight[i] >= 0:
                    include = profit[i] + dp[i][c-weight[i]]
                dp[i][c] = max(skip_p, include)
        return dp[N-1][M-1]
                
if __name__ == "__main__":
    sol = Solution()
    profits = [4, 4, 7, 1]
    weights = [5, 2, 3, 1]
    capacity = 8
    print(sol.get_maximum_profit(profits, weights, capacity))
    