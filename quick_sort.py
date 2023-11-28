class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def quickSort(self, pairs) :
        pn = Pair(float("+inf"), "infinity")
        pairs.append(pn)
        low = 0
        high = len(pairs)-1
        self.quickSortHelper(pairs, low, high)
        del pairs[-1]

    def quickSortHelper(self, pairs, low, high) :
        if low < high:
            pos = self.partition(pairs, low, high)
            self.quickSortHelper(pairs, low, pos-1)
            self.quickSortHelper(pairs, pos+1, high)
    
    def partition(self, pairs, low, high):
        pivot = low
        pv = pairs[pivot]
        while low < high:
            while pairs[low].key <= pv.key:
                low += 1
            while pairs[high].key > pv.key:
                high -= 1
            if low < high:
                pairs[low], pairs[high] = pairs[high], pairs[low]
        pairs[high], pairs[pivot] = pairs[pivot], pairs[high]
        return high

            
if __name__ == "__main__":
    def tc1():
        qs = Solution()
        p1 = Pair(5, "apple")
        p2 = Pair(2, "banana")
        p3 = Pair(9, "cherry")
        p4 = Pair(1, "date")
        p5 = Pair(9, "elderberry")
        input = [p1, p2, p3, p4, p5]
        print(input)
        qs.quickSort(input)
        sorted_print = [(r.key,r.value) for r in input]
        print(sorted_print)
        
    def tc2():
        qs = Solution()
        p1 = Pair(3, "cat")
        p2 = Pair(2, "dog")
        p3 = Pair(3, "bird")
        input = [p1, p2, p3]
        print(input)
        qs.quickSort(input)
        sorted_print = [(r.key,r.value) for r in input]
        print(sorted_print)
    tc2()       
    tc1()