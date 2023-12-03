import heapq

class DisjointSet:
    def __init__(self, n:int) -> None:
        self.storage = [-1]*n
        self.size = [1]*n
        self.num_of_sets = n
    
    # find the root component of x
    def find(self, x:int) -> int:
        while self.storage[x] >= 0:
            x = self.storage[x]
        return x
    
    # will return if x and y belong to the same set
    def is_same_set(self, x:int, y:int) -> bool:
        if self.find(x) == self.find(y):
            return True
        return False
    
    # will union the sets that x and y are in and returns True, 
    # if x and y are already in the same set it will form a cycle 
    # so it will not union, return False instead
    def union(self, x:int, y:int) -> bool:
        if self.is_same_set(x, y):
            return False
        xp = self.find(x)
        yp = self.find(y)
        if self.size[xp] >= self.size[yp]:
            self.size[xp] += self.size[yp]
            self.storage[yp] = xp
        else:
            self.size[yp] += self.size[xp]
            self.storage[xp] = yp
        self.num_of_sets -= 1
        return True
        
        
    def get_num_of_sets(self) -> int:
        return self.num_of_sets
    

class Kruskals:
    def __init__(self) -> None:
        pass
    
    # return the weight of the min spanning tree
    def find_min_spanning_tree(self, n:int, edges:list) -> int:
        # we first setup the min heap to get the least costing edges
        mheap = []
        for f, t, w in edges:
            heapq.heappush(mheap, (w, f, t))
        # initialize the disjoint set for the incoming vertices
        ds = DisjointSet(n)
        total_w = 0
        # calculate the total weight after union of all the edges
        while mheap:
            w, f, t = heapq.heappop(mheap)
            if ds.union(f, t):
                total_w += w
        return total_w if ds.get_num_of_sets() == 1 else -1
