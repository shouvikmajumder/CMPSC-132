# LAB 5
5# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    '''
        >>> my_tree = BinarySearchTree() 
        >>> my_tree.isEmpty()
        True
        >>> my_tree.insert(9) 
        >>> my_tree.insert(5) 
        >>> my_tree.insert(14) 
        >>> my_tree.insert(4)  
        >>> my_tree.insert(6) 
        >>> my_tree.insert(5.5) 
        >>> my_tree.insert(7)   
        >>> my_tree.insert(25) 
        >>> my_tree.insert(23) 
        >>> my_tree.getMin
        4
        >>> my_tree.getMax
        25
        >>> 67 in my_tree
        False
        >>> 5.5 in my_tree
        True
        >>> my_tree.isEmpty()
        False
        >>> my_tree.getHeight(my_tree.root)   # Height of the tree
        3
        >>> my_tree.getHeight(my_tree.root.left.right)
        1
        >>> my_tree.getHeight(my_tree.root.right)
        2
        >>> my_tree.getHeight(my_tree.root.right.right)
        1
        >>> my_tree.get_closest(18) 
        14
        >>> my_tree.get_closest(19) 
        23
        >>> my_tree.get_closest(5)  
        5
        >>> my_tree.get_closest(72) 
        25
        >>> my_tree.get_closest(7)  
        7
        >>> my_tree.get_closest(8) 
        9
    '''
    def __init__(self):
        self.root = None


    def insert(self, value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if(value<node.value):
            if(node.left==None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:   
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    
    def isEmpty(self):
        # YOUR CODE STARTS HERE
        if self.root == None:
            return True
        return False

    @property
    def getMin(self): 
        # YOUR CODE STARTS HERE
        curr = self.root
        if self.isEmpty():
            return None
        while curr != None:
            if curr.left == None:
                return curr.value
            curr= curr.left
                    
    @property
    def getMax(self): 
        # YOUR CODE STARTS HERE  
        curr = self.root
        if self.isEmpty():
            return None
        while curr != None:
            if curr.right == None:
                return curr.value
            curr = curr.right
            
    
    def __contains__(self,value):
        # YOUR CODE STARTS HERE
        curr = self.root
        while curr != None:
            if curr.value == value:
                return True
            elif value>=curr.value:
                curr = curr.right
                if curr.right == None:    
                    if curr.value == value:
                        return True
                    return False
            elif value<curr.value:
                curr = curr.left
                if curr.left == None:        
                    if curr.value == value:
                        return True 
                    return False

                

    def getHeight(self, node):
        # YOUR CODE STARTS HERE
        if node == None:
            return -1
        left = self.getHeight(node.left) + 1
        right = self.getHeight(node.right) + 1
        if right>left:
            return right
        else:
            return left
        

    def get_closest(self, item):
        # YOUR CODE STARTS HERE
        curr = self.root
        difference = float("inf")
        value = None 
        while curr != None:
            if item == curr.value:
                return curr.value
            if abs(item-curr.value)<difference:
                value = curr.value
                difference = abs(item-curr.value)
            if item> curr.value:
                curr = curr.right
            elif item<curr.value:
                curr = curr.left
        return value




if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
    # doctest.run_docstring_examples(.calculate, globals(), name='LAB5',verbose=True)

