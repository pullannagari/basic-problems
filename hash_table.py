from collections import deque

class HashTable:
    def __init__(self) -> None:
        self.storage = [None]*10
    
    def hash_function(self, k):
        if not k:
            return
        return abs(k%10)
    
    def add(self, k, v) -> None:
        if not k or not v:
            return
        hash_val = self.hash_function(k)
        if not self.storage[hash_val]:
            ll = deque()
            ll.append((k,v))
            self.storage[hash_val] = ll
        else:
            update = False
            ll = self.storage[hash_val]
            for item in ll:
                if item[0] == k:
                    item[1] = v
                    update = True
            if not update:
                ll.append((k,v))
    
    def get(self, k) -> int:
        if not k:
            return
        hash_val = self.hash_function(k)
        if not self.storage[hash_val]:
            return -1
        ll:deque = self.storage[hash_val]
        for item in ll:
            if item[0] == k:
                return item[1]
        return -1
    
    def delete(self, k) -> None:
        if not k:
            return -1
        hash_val = self.hash_function(k)
        if not self.storage[hash_val]:
            return -1
        ll:deque = self.storage[hash_val]
        for item in ll:
            if item[0] == k:
                v = item[1]
                ll.remove((k,v))
                return v
        return -1
    
    def get_values(self) -> deque:
        pass
    
    def get_keys(self) -> deque:
        pass
    
if __name__ == "__main__":
    ht = HashTable()
    ht.add(1, "one")
    ht.add(2, "two")
    ht.add(12, "twelve")
    ht.add(3, "three")
    print(ht.get(2))
    print(ht.get(3))
    print(ht.get(12))
    print(ht.delete(2))
    print(ht.get(2))