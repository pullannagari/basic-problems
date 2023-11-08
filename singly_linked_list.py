class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:
        if index < 0:
            return -1
        curr_node = self.head
        curr_index = 0
        while curr_index < index:
            if not curr_node:
                return -1
            curr_node = curr_node.next
            curr_index += 1
        if not curr_node:
            return -1
        return curr_node.val


        

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index < 0:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        curr_index = 0
        curr_node = self.head
        while curr_index < index-1:
            if not curr_node:
                return False
            curr_node = curr_node.next
            curr_index +=1
        if curr_node:
            if curr_node.next:
                if curr_node.next == self.tail:
                    self.tail = curr_node
                curr_node.next = curr_node.next.next
                return True
        return False

        

    def getValues(self) -> list(int):
        curr_node = self.head
        ret = []
        while curr_node:
            ret.append(curr_node.val)
            curr_node = curr_node.next
        return ret
        
