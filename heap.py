class Heap:
    def __init__(self) -> None:
        self.storage = []
        
    def _swap_and_adjust(self, dir):
        if dir == "up":
            index = len(self.storage)-1
            while index > 0:
                par_index = index // 2
                if self.storage[par_index] > self.storage[index]:
                    self.storage[par_index], self.storage[index] = self.storage[index], self.storage[par_index]
                index = par_index
        elif dir == "down":
            index = 0
            length = len(self.storage)-1
            while index < len(self.storage):
                left = index * 2 + 1
                right = index * 2 + 2
                if left <= length and right <= length:
                    if self.storage[left] < self.storage[right]:
                        if self.storage[left] < self.storage[index]:
                            self.storage[index], self.storage[left] = self.storage[left], self.storage[index]
                            index = left
                        else:
                            return
                    else:
                        if self.storage[right] < self.storage[index]:
                            self.storage[index], self.storage[right] = self.storage[right], self.storage[index]
                            index = right
                        else:
                            return
                elif left <= length:
                    if self.storage[left] < self.storage[index]:
                        self.storage[index], self.storage[left] = self.storage[left], self.storage[index]
                        index = left
                    else:
                        return
                else:
                    return
                
    
    def push(self, val: int) -> None:
        self.storage.append(val)
        if len(self.storage) == 1:
            return
        self._swap_and_adjust("up")
            
    
    def peek(self) -> int:
        if self.storage:
            return self.storage[0]
        return -1
    
    def pop(self) -> int:
        if not self.storage:
            return -1
        val = self.storage[0]
        self.storage[0] = self.storage[len(self.storage)-1]
        self.storage.pop()
        if not self.storage:
            return val
        self._swap_and_adjust("down")
        return val