# queue is first in first out
# dequeue is fifo and can also remove the elements from both the ends
class Dequeue:
    
    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.storage = [None]*10
    
    def pop_left(self) -> int:
        curr_val = None
        if self.left is not None:
            curr_val = self.storage[self.left]
        if curr_val is None:
            return -1 # left is already None
        elif self.left == self.right:
            self.storage[self.left] = None
        elif self.left == len(self.storage) - 1:
            self.storage[self.left] = None
            self.left = 0
        elif self.left >= 0:
            self.storage[self.left] = None
            self.left += 1
        return curr_val
                
    
    def push_left(self, val: int):
        if self.left is None:
            self.left = 0
            self.right = 0
        else:
            if self.left == 0:
                self.left = len(self.storage)-1
            else:
                if self.left-1 > self.right:
                    self.left = self.left -1
                else:
                    return -1 # queue full
        self.storage[self.left] = val
            
    
    def peek_left(self) -> int:
        if self.left is not None:
            return self.storage[self.left]
        return -1
    
    def peek_right(self) -> int:
        if self.right is not None:
            return self.storage[self.right]
        
    def push_right(self, val: int):
        if self.right is None:
            self.right = 0
            self.left = 0
            self.storage[self.right] = val
        else:
            if self.left > 0:
                if self.right+1 >= self.left:
                    return -1 # queue full
            self.right += 1
            self.storage[self.right] = val
        
    
    def pop_right(self):
        curr_val = None
        if self.right is not None:
            curr_val = self.storage[self.right]
        if not curr_val:
            return -1
        elif self.left == self.right:
            self.storage[self.right] = None
        elif self.right > self.left:
            self.storage[self.right] = None
            self.right -= 1
        return curr_val
    
if __name__ == "__main__":
    dq = Dequeue()
    dq.push_left(10)
    assert dq.peek_right() == dq.peek_left()
    dq.push_right(20)
    dq.push_right(22)
    dq.push_right(25)
    assert dq.peek_right() != dq.peek_left()
    assert dq.peek_right() == 25
    dq.push_left(30)
    dq.push_left(50)
    dq.push_left(8)
    dq.push_right(9)
    dq.push_right(10)
    assert not dq.push_right(11) == -1
    assert dq.push_right(100) == -1
    assert dq.peek_left() == 8
    assert dq.pop_left() == 8
    assert dq.push_right(100) != -1
    assert dq.pop_left() == 50
    assert dq.pop_left() == 30
    assert dq.pop_left() == 10
    assert dq.pop_left() == 20
    assert dq.pop_right() == 100
    
    
    
    
    