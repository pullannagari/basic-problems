class STNode:
    
    def __init__(self, L:int, R: int, sum: int) -> None:
        self.L = L
        self.R = R
        self.left = None
        self.right = None
        self.sum = sum

class SegmentTree:
    
    def __init__(self, nums: list):
        self.root = self.initialize(0, len(nums)-1, nums)

    def initialize(self, L:int, R:int, nums: list):
        if L == R:
            return STNode(L, L, nums[L])
        root = STNode(L, R, 0)
        mid = (L + R)//2
        root.left = self.initialize(L, mid, nums)
        root.right = self.initialize(mid+1, R, nums)
        root.sum = root.left.sum + root.right.sum
        return root
    
    def update(self, index: int, val: int) -> None:
        self.update_helper(index, val, self.root)
        
    def update_helper(self, index: int, val: int, curr: STNode) -> None:
        L = curr.L
        R = curr.R
        if L == R and L == index:
            curr.sum = val
            return
        mid = (L+R)//2
        if index <= mid:
            self.update_helper(index, val, curr.left)
        else:
            self.update_helper(index, val, curr.right)
        curr.sum = curr.left.sum + curr.right.sum
    
    def query(self, L: int, R: int) -> int:
        return self.query_helper(L, R, self.root)
    
    def query_helper(self, L:int, R:int, curr: STNode) -> int:
        currL = curr.L
        currR = curr.R
        if L == currL and R == currR:
            return curr.sum
        mid = (currL + currR) // 2
        if L > mid:
            return self.query_helper(L, R, curr.right)
        elif R <= mid:
            return self.query_helper(L, R, curr.left)
        else:
            return (self.query_helper(L, mid, curr.left) + self.query_helper(mid+1, R, curr.right))
        
if __name__ == "__main__":
    st = SegmentTree([1, 2, 3, 4, 5])
    st.update(2, 6)
    print(st.query(2, 4))
    print(st.query(0, 4))
