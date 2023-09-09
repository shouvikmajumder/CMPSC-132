# LAB4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node: # You are not allowed to modify this class
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return f"Node({self.value})"

    __repr__ = __str__
                        
                          
class SortedLinkedList:
    ''' 
        >>> x=SortedLinkedList()
        >>> x.add(8.76)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(5)
        >>> x.add(3)
        >>> x.add(-7.5)
        >>> x.add(4)
        >>> x.add(9.78)
        >>> x.add(4)
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.removeDuplicates()
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 3 -> 4 -> 5 -> 8.76 -> 9.78
        >>> sub1, sub2 = x.split()
        >>> sub1
        Head:Node(-7.5)
        Tail:Node(4)
        List:-7.5 -> 1 -> 3 -> 4
        >>> sub2
        Head:Node(5)
        Tail:Node(9.78)
        List:5 -> 8.76 -> 9.78
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 3 -> 4 -> 5 -> 8.76 -> 9.78
    '''

    def __init__(self):   # You are not allowed to modify the constructor
        self.head=None
        self.tail=None

    def __str__(self):   # You are not allowed to modify this method
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out) 
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__=__str__


    def isEmpty(self):
        return self.head == None

    def __len__(self):
        count=0
        current=self.head
        while current:
            current=current.next
            count+=1
        return count

                
    def add(self, value):
        # --- YOUR CODE STARTS HERE
        newnode = Node(value)
        if self.isEmpty():
            self.head = newnode
            self.tail = newnode
        temp = self.head
        while temp != None:
            if self.head.value >= newnode.value:
                newnode.next = temp
                self.head = newnode     
                return None            
            elif temp.value<= newnode.value and temp.next.value>=newnode.value:   
                newnode.next = temp.next
                temp.next = newnode
                return None 
            elif self.tail.value <= newnode.value:
                self.tail.next = newnode
                self.tail = newnode
                return None 
            temp = temp.next
                    

    def split(self):
        # --- YOUR CODE STARTS HERE
        first_part = SortedLinkedList()
        second_part = SortedLinkedList()
        if self.isEmpty():
            return None
        if self.__len__() % 2 != 0:
            temp = self.head
            count = 0
            while count != ((self.__len__()//2)+1):
                first_part.add(temp.value)
                count += 1
                temp = temp.next
            while count< self.__len__():
                second_part.add(temp.value)
                count += 1 
                temp = temp.next
            return first_part, second_part 
        
        if self.__len__()%2 == 0:
            temp = self.head 
            count = 0
            while count != (self.__len__()/2):
                first_part.add(temp.value)
                count += 1
                temp = temp.next
            while count< self.__len__():
                second_part.add(temp.value)
                count += 1 
                temp = temp.next
            return first_part, second_part 


    def removeDuplicates(self):
        # --- YOUR CODE STARTS HERE
        temp = self.head
        while temp != None:
            if temp.next != None and temp.value == temp.next.value:
                temp.next = temp.next.next 
            else: 
                temp = temp.next
            

def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace intersection with the name of the function you want to test
    # doctest.run_docstring_examples(SortedLinkedList, globals(), name='LAB4',verbose=True)

if __name__ == "__main__":
    run_tests()
