import heapq
# dijkstra's algorithm to calculate shortest path
# we can't use regular BFS to explore all the nodes level by level and find the shortest path since there are weights
# we instead use dijkstra's which is kind of a BFS, but uses minheap instead of a queue to find the next node
# time complexity is ElogV where E is edges and V is vertices
class Solution:
    def shortestPath(self, n: int, edges: list, src: int) -> dict:
        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        for edge in edges:
            adj_list[edge[0]].append((edge[1], edge[2]))
        shortest = {}
        mheap = [(0,src)]
        while mheap:
            w1, n1 = heapq.heappop(mheap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            for n2, w2 in adj_list[n1]:
                if n2 not in shortest:
                    heapq.heappush(mheap, (w1+w2, n2))
        # at the end, we should also add the nodes which are unreachable
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return shortest
    
if __name__ == "__main__":
    sol = Solution()
    edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]]
    print(sol.shortestPath(5, edges, 0))