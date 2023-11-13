from collections import deque

class HashTable:
    def __init__(self) -> None:
        self.storage = [None]*10
    
    def hash_function(self, k):
        if k is None:
            return
        return abs(k%10)
    
    def add(self, key, value) -> None:
        if key is None or value is None:
            return
        hash_val = self.hash_function(key)
        if self.storage[hash_val] is None:
            ll = deque()
            ll.append((key,value))
            self.storage[hash_val] = ll
        else:
            update = False
            ll = self.storage[hash_val]
            for item in ll:
                if item[0] == key:
                    item[1] = value
                    update = True
            if not update:
                ll.append((key,value))
    
    def get(self, key) -> int:
        if key is None:
            return
        hash_val = self.hash_function(key)
        if self.storage[hash_val] is None:
            return -1
        ll:deque = self.storage[hash_val]
        for item in ll:
            if item[0] == key:
                return item[1]
        return -1
    
    def delete(self, key) -> None:
        if key is None:
            return -1
        hash_val = self.hash_function(key)
        if self.storage[hash_val] is None:
            return -1
        ll:deque = self.storage[hash_val]
        for item in ll:
            if item[0] == key:
                v = item[1]
                ll.remove((key,v))
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
    print(ht.get(12))