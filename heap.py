class MinHeap:
    
    def __init__(self):
        self.storage = []

    def push(self, val: int) -> None:
        self.storage.append(val)
        curr_index = len(self.storage)-1
        while curr_index > 0:
            par_index = (curr_index -1) // 2
            if self.storage[par_index] > self.storage[curr_index]:
                self.storage[par_index], self.storage[curr_index] = self.storage[curr_index], self.storage[par_index]
            curr_index = par_index

    def down_propagation_helper(self, curr_index:int) -> None:
        while curr_index < len(self.storage):
            left = curr_index * 2 + 1
            right = curr_index * 2 + 2
            if left < len(self.storage) and right < len(self.storage):
                if self.storage[left] < self.storage[right]:
                    if self.storage[left] < self.storage[curr_index]:
                        self.storage[left], self.storage[curr_index] = self.storage[curr_index], self.storage[left]
                    curr_index = left
                else:
                    if self.storage[right] < self.storage[curr_index]:
                        self.storage[right], self.storage[curr_index] = self.storage[curr_index], self.storage[right]
                    curr_index = right
            elif left < len(self.storage):
                if self.storage[left] < self.storage[curr_index]:
                    self.storage[left], self.storage[curr_index] = self.storage[curr_index], self.storage[left]
                curr_index = left
            else:
                break

    def pop(self) -> int:
        if len(self.storage) > 1:
            ret_val = self.storage[0]
            repl_val = self.storage.pop()
            self.storage[0] = repl_val
            curr_index = 0
            self.down_propagation_helper(curr_index)
            return ret_val
        elif len(self.storage) == 1:
            return self.storage.pop()
        else:
            return -1

    def top(self) -> int:
        if self.storage:
            return self.storage[0]
        return -1
        

    def heapify(self, nums: list) -> None:
        if nums:
            self.storage = nums
            curr_index = len(self.storage)//2
            while curr_index >= 0:
                self.down_propagation_helper(curr_index)
                curr_index -= 1
        
    
if __name__ == "__main__":
    def tc1():
        hp = MinHeap()
        hp.push(1)
        assert hp.top() == 1
        assert hp.pop() == 1
        assert hp.pop() == -1
    def tc2():
        hp = MinHeap()
        hp.push(1)
        hp.push(2)
        assert hp.pop() == 1
        assert hp.pop() == 2
    def tc3():
        hp = MinHeap()
        hp.heapify([1,2,3,4,5])
        assert hp.pop() == 1
        assert hp.pop() == 2
        assert hp.pop() == 3
        assert hp.pop() == 4
        assert hp.pop() == 5
    def tc4():
        hp = MinHeap()
        hp.push(5)
        hp.push(2)
        hp.push(10)
        assert hp.top() == 2
        assert hp.pop() == 2
        assert hp.top() == 5
        assert hp.pop() == 5
        assert hp.top() == 10
        assert hp.pop() == 10
        assert hp.top() == -1
        assert hp.pop() == -1
    def tc5():
        hp = MinHeap()
        hp.heapify([5, 4, 3, 2, 1])
        assert hp.pop() == 1
        assert hp.top() == 2
    def tc6():
        hp = MinHeap()
        hp.heapify([3, 2, 1])
        assert hp.pop() == 1
        assert hp.top() == 2
        assert hp.pop() == 2
        assert hp.top() == 3
    def tc7():
        hp = MinHeap()
        hp.push(10)
        hp.heapify([5,3,7])
        assert hp.pop() == 3
        assert hp.top() == 5
    def tc8():
        hp = MinHeap()
        hp.heapify([])
        assert hp.pop() == -1
    tc1()
    tc2()
    tc3()
    tc4()
    tc5()
    tc6()
    tc7()
    tc8()
