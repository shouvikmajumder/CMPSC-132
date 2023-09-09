class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 


    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__

class LinkedList:
    '''
    >>> lst = LinkedList()
    >>> lst.add(4) 
    >>> lst.add(5) 
    >>> lst.add(6) 
    >>> lst
    Head:Node(6)
    Tail:Node(4)
    List:6 -> 5 -> 4
    >>> lst.duplicate(6)
    >>> lst
    Head:Node(6)
    Tail:Node(4)
    List:6 -> 6 -> 5 -> 4
    >>> lst.duplicate(13) 
    >>> lst
    Head:Node(6)
    Tail:Node(4)
    List:6 -> 6 -> 5 -> 4
    >>> lst.add(1) 
    >>> lst.duplicate(6)  
    >>> lst
    Head:Node(1)
    Tail:Node(4)
    List:1 -> 6 -> 6 -> 6 -> 6 -> 5 -> 4
    >>> lst.duplicate(4) 
    >>> lst
    Head:Node(1)
    Tail:Node(4)
    List:1 -> 6 -> 6 -> 6 -> 6 -> 5 -> 4 -> 4
    '''

    
    def __init__(self):
        self.head=None
        self.tail=None

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out)
        return 'Head:{}\nTail:{}\nList:{}'.format(self.head,self.tail,out)

    __repr__=__str__

    def isEmpty(self):
        return self.head==None


    def __len__(self):
        current=self.head
        count=0
        while current is not None:
            count += 1
            current = current.next    
        return count


    def add(self, value):
        newNode=Node(value)
        if self.isEmpty():
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    


    def duplicate(self, item):
        # YOUR CODE STARTS HERE
        temp = self.head
        while temp != None: 
            if temp.value == item:
                newnode = Node(item)
                newnode.next = temp.next
                temp.next = newnode
                temp = temp.next.next
            else:
                temp= temp.next   
        return None 

            
def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace intersection with the name of the function you want to test
    # doctest.run_docstring_examples(LinkedList, globals(), name='recetation 6.py',verbose=True)
    
if __name__ == "__main__":
    run_tests()
