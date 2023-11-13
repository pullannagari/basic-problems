# BST
# has a root node
# each node has at most 2 children
# left child val is less than the parent val
# right child val is greater than the parent val
# operations
# insert(val)
# delete(val) # find and delete node
# search(val) # find the node with val

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return
        else:
            curr_node = self.root
            while curr_node:
                if val < curr_node.val:
                    if curr_node.left is not None:
                        curr_node = curr_node.left
                    else:
                        curr_node.left = new_node
                        return
                else:
                    if curr_node.right is not None:
                        curr_node = curr_node.right
                    else:
                        curr_node.right = new_node
                        return
                    
    def search(self, val):
        if not self.root:
            return -1
        else:
            curr_node = self.root
            while curr_node:
                if curr_node.val == val:
                    return curr_node
                elif curr_node.val < val:
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right
        return -1
    
    def successor(self, node: Node, left_or_right: str):
        if not node:
            return None
        currNode = node
        while currNode:
            if currNode.left:
                currNode = currNode.left
            else:
                return currNode

    def deleteNode(self, root: Node, key: int) -> Node:
        if not root:
            return None
        if root.val == key:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                succ_node = self.successor(root.right, "right")
                root.val = succ_node.val
                root.right = self.deleteNode(root.right, succ_node.val)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
    
    def delete(self, key) -> Node:
        return self.deleteNode(self.root, key=key)
        
        # doesn't handle finding the correct successor and replacement
        # if not self.root:
        #     return False
        # else:
        #     curr_node = self.root
        #     is_deleted = False
        #     while curr_node:
        #         if curr_node.val == key or is_deleted:    
        #             if curr_node.right:
        #                 curr_node.val = curr_node.right.val
        #                 repl_node = curr_node.right
        #                 if not repl_node.left and not repl_node.right:
        #                     curr_node.right = None
        #                     curr_node = curr_node.right
        #                 else:
        #                     curr_node = repl_node
        #             elif curr_node.left:
        #                 curr_node.val = curr_node.left.val
        #                 repl_node = curr_node.left
        #                 if not repl_node.left and not repl_node.right:
        #                     curr_node.left = None
        #                     curr_node = curr_node.left
        #                 else:
        #                     curr_node = repl_node
        #             else:
        #                 curr_node = None
        #             is_deleted = True
        #         if not is_deleted:
        #             par_node = curr_node
        #             if key < curr_node.val:
        #                 curr_node = curr_node.left
        #             else:
        #                 curr_node = curr_node.right
        #             if curr_node and curr_node.val == key:
        #                     if not curr_node.left and not curr_node.right:
        #                         par_node.left = None
        #                         return
        #     return is_deleted       
                

    def in_order(self, curr):
        if not curr:
            return
        else:
            self.in_order(curr.left)
            print(curr.val)
            self.in_order(curr.right)
            
    def pre_order(self, curr):
        if not curr:
            return
        else:
            print(curr.val)
            self.pre_order(curr.left)
            self.pre_order(curr.right)
            
    def post_order(self, curr):
        if not curr:
            return
        else:
            self.post_order(curr.left)
            self.post_order(curr.right)
            print(curr.val)
            

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(30)
    bst.insert(21)
    bst.insert(50)
    bst.insert(15)
    bst.insert(25)
    bst.in_order(bst.root)
    print("-"*90)
    bst.pre_order(bst.root)
    print("-"*90)
    bst.post_order(bst.root)
    print("-"*90)
    bst.insert(55)
    bst.pre_order(bst.root)
    print("-"*90)
    bst.insert(22)
    bst.pre_order(bst.root)
    print("-"*90)
    bst.delete(22)
    bst.pre_order(bst.root)
    print("-"*90)
    bst.delete(21)
    bst.pre_order(bst.root)
    print("-"*90)
    bst.delete(30)
    bst.pre_order(bst.root)
    print("-"*90)