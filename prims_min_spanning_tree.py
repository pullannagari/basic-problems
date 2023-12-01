import heapq

# used to find the minimum spanning tree
# minimum spanning tree is a tree which has the following properties
# min cost
# all nodes/vertices connected
# undirected
# acyclic
# uses the similar strategy as the dijkstra's shortest path(BFS variation)
# weight is not aggregated, rather calculated for individul nodes
# time complexity is ElogV where E is the edges and V is the vertices
class Solution:
    def minimumSpanningTree(self, n: int, edges: list) -> int:
        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        for f, t, w in edges:
            adj_list[f].append((t,w))
            adj_list[t].append((f,w))
        mst = []
        visited = set()
        mheap = [(0,0,0)]
        total_weight = 0
        while mheap:
            edge = heapq.heappop(mheap)
            if edge[2] not in visited:
                visited.add(edge[2])
                mst.append(edge)
                total_weight += edge[0]
                for n2, w in adj_list[edge[2]]:
                    if n2 not in visited:
                        heapq.heappush(mheap,(w, edge[2],n2))
        for i in range(n):
            if i not in visited:
                return -1
        return total_weight