class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class MergeSort:
    def __init__(self) -> None:
        pass
    
    def mergeSort(self, pairs):
        if len(pairs) <= 1:
            return pairs
        mid = len(pairs)//2
        left = self.mergeSort(pairs[:mid])
        right = self.mergeSort(pairs[mid:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        i, j = 0, 0
        result = []
        while i < len(left) and j < len(right):
            if left[i].key < right[j].key:
                result.append(left[i])
                i += 1
            elif left[i].key > right[j].key:
                result.append(right[j])
                j += 1
            else:
                result.append(left[i])
                result.append(right[j])
                i += 1
                j += 1
        if i < len(left):
            result.extend(left[i:])
        if j < len(right):
            result.extend(right[j:])
        return result
            
         
if __name__ == "__main__":
    ms = MergeSort()
    p1 = Pair(5, "apple")
    p2 = Pair(2, "banana")
    p3 = Pair(9, "cherry")
    p4 = Pair(1, "date")
    p5 = Pair(9, "elderberry")
    input = [p1, p2, p3, p4, p5]
    print(input)
    sorted = ms.mergeSort(input)
    sorted_print = [(r.key,r.value) for r in sorted]
    print(sorted_print)