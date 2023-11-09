class DynamicArray:
    
    def __init__(self, capacity: int):
        self.storage = [None]*capacity
        self.end_index_stack = []
        self.size = 0


    def get(self, i: int) -> int:
        return self.storage[i]


    def set(self, i: int, n: int) -> None:
        if len(self.end_index_stack) == 0:
            self.end_index_stack.append(i)
            self.size += 1
        elif self.end_index_stack[-1] < i:
            self.end_index_stack.append(i)
        if self.storage[i] is None:
            self.size += 1
        self.storage[i] = n
        

    def pushback(self, n: int) -> None:
        if len(self.end_index_stack) == 0:
            index = 0
        else:
            index = self.end_index_stack[-1]+1
        if index == len(self.storage):
            self.resize()
        self.storage[index] = n
        self.end_index_stack.append(index)
        self.size += 1


    def popback(self) -> int:
        index = self.end_index_stack.pop()
        ret_val = self.storage[index]
        self.size -= 1
        return ret_val
 

    def resize(self) -> None:
        cap = len(self.storage)
        new_storage = [None]*cap
        self.storage.extend(new_storage)

    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return len(self.storage)
