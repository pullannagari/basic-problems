# disjoint sets are used to find if there is a cycle in the given edge list
# we represent the disjoint set using an array, where:
#   array index represents the value of the vertex/node and 
#   index value represents the parent 
# the operations on a disjoint set are defined as below:
# find() to find if the given edge has the same root/absolute parent
# union() merges the edge if if doesn't form a cycle
# find_cycle() to check if there exists a cycle given the edges
class Disjoint:
    def __init__(self, cap) -> None:
        self.storage = [-1]*cap
        
    def _find_parent(self, node):
        while self.storage[node] >= 0:
            node = self.storage[node]
        return node
    
    def find(self, frm:int, to:int) -> bool:
        return self._find_parent(frm) == self._find_parent(to)
    
    def find_cycle(self) -> bool:
        pass
    
    def union(self, frm:int, to:int) -> None:
        if not self.find(frm, to):
            frm_par = self._find_parent(frm)
            to_par = self._find_parent(to)
            if abs(self.storage[frm_par]) >= abs(self.storage[to_par]):
                self.storage[frm_par] -= abs(self.storage[to_par])
                self.storage[to_par] = frm_par
            else:
                self.storage[to_par] -= 1
                self.storage[frm_par] = to_par
            
class UnionFind:
    def __init__(self, n) -> None:
        self.storage = [-1]*n
        self.size = n
        

    def find(self, x: int) -> int:
        # collapsing the tree for optimizing find
        if self.storage[x] >= 0:
            self.storage[x] = self.find(self.storage[x])
            return self.storage[x]
        return x


    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


    def union(self, x: int, y: int) -> bool:
        if not self.isSameComponent(x, y):
            frm_par = self.find(x)
            to_par = self.find(y)
            self.size -= 1
            if abs(self.storage[frm_par]) >= abs(self.storage[to_par]):
                self.storage[frm_par] -= abs(self.storage[to_par])
                self.storage[to_par] = frm_par
            else:
                self.storage[to_par] -= abs(self.storage[frm_par])
                self.storage[frm_par] = to_par
            return True
        return False
        

    def getNumComponents(self) -> int:
        return self.size

if __name__ == "__main__":
    
    def test3():
        ["UnionFind", 10, "find", 1, "isSameComponent", 1, 3, "union", 1, 2, "union", 2, 3, "getNumComponents", "isSameComponent", 1, 3]
        cap = 10
        uf = UnionFind(cap)
        assert uf.find(1) == 1
        assert not uf.isSameComponent(1,3)
        uf.union(1,2)
        uf.union(2,3)
        uf.union(5,3)
        uf.union(5,6)
        assert uf.getNumComponents() == 6
        assert uf.isSameComponent(6,1)
        
    
    def test2():
        cap = 1
        ds = Disjoint(cap)
        ds.storage = [2,2,-3,5,3,-3]
        ds.union(2,5)
        print(ds.storage)
    
    def test1():
        cap = 10
        ds = Disjoint(cap)
        for i in range(0, cap):
            j = i + 1
            if i == cap-1:
                j = 0
            print(i, j)
            ds.union(i, j)
        print(ds.storage)
        
    test3()
    