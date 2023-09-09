# LAB7
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement

class MaxBinaryHeap:
    '''
        >>> h = MaxBinaryHeap()
        >>> h.getMax
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [10, 5]
        >>> h.insert(14)
        >>> h._heap
        [14, 5, 10]
        >>> h.insert(9)
        >>> h
        [14, 9, 10, 5]
        >>> h.insert(2)
        >>> h
        [14, 9, 10, 5, 2]
        >>> h.insert(11)
        >>> h
        [14, 9, 11, 5, 2, 10]
        >>> h.insert(14)
        >>> h
        [14, 9, 14, 5, 2, 10, 11]
        >>> h.insert(20)
        >>> h
        [20, 14, 14, 9, 2, 10, 11, 5]
        >>> h.insert(20)
        >>> h
        [20, 20, 14, 14, 2, 10, 11, 5, 9]
        >>> h.getMax
        20
        >>> h._leftChild(1)
        20
        >>> h._rightChild(1)
        14
        >>> h._parent(1)
        >>> h._parent(6)
        14
        >>> h._leftChild(6)
        >>> h._rightChild(9)
        >>> h.deleteMax()
        20
        >>> h._heap
        [20, 14, 14, 9, 2, 10, 11, 5]
        >>> h.deleteMax()
        20
        >>> h
        [14, 9, 14, 5, 2, 10, 11]
        >>> len(h)
        7
        >>> h.getMax
        14
    '''

    def __init__(self):
        self._heap=[]
        
    def __str__(self):
        return f'{self._heap}'

    __repr__=__str__

    def __len__(self):
        return len(self._heap)

    @property
    def getMax(self):
        # YOUR CODE STARTS HERE
        if len(self) == 0:
            return None
        else:
            return self._heap[0]
    
    def _parent(self, index):
        parent_index = index // 2
        if parent_index >= 1:
            return self._heap[parent_index - 1]
        else:
            return None     
   
    def _leftChild(self,index):
        # YOUR CODE STARTS HERE
        try:
            return self._heap[(index*2)-1]
        except:
            return None

    def _rightChild(self,index):
        # YOUR CODE STARTS HERE
        try:
            return self._heap[(index*2)]
        except:
            return None


    def insert(self, item):
        self._heap.append(item)
        item_heap_index = len(self._heap)

        while item_heap_index > 1 and self._parent(item_heap_index) < item:
            parent_heap_index = item_heap_index // 2
            self._heap[item_heap_index - 1] = self._parent(item_heap_index)
            item_heap_index = parent_heap_index

        self._heap[item_heap_index - 1] = item


    def deleteMax(self):
        if self._rightChild == self._rightChild and self._leftChild == self._leftChild:
            if len(self) == 0:
                return None
            elif len(self) == 1:
                removed = self._heap[0]
                self._heap = []
                return removed
            else:
                max = self._heap[0]
                self._heap[0] = self._heap.pop()
                current = 0
                L = 1
                R = 2
                while L < len(self._heap):
                    max_child = L
                    if R < len(self._heap) and self._heap[R] > self._heap[L]:
                        max_child = R
                    if self._heap[current] < self._heap[max_child]:
                        self._heap[current], self._heap[max_child] = self._heap[max_child], self._heap[current]
                        current = max_child
                        L = current * 2 + 1
                        R = current * 2 + 2
                    else:
                        L = len(self._heap)
                return max
                

def heapSort(numList):
    '''
    >>> heapSort([9,1,7,4,1,2,4,8,7,0,-1,0])
    [9, 8, 7, 7, 4, 4, 2, 1, 1, 0, 0, -1]
    >>> heapSort([9,1,7,4,1,2,4,8,7,0,-1,0])
    [9, 8, 7, 7, 4, 4, 2, 1, 1, 0, 0, -1]
    >>> heapSort([-15, 1, 0, -15, -15, 8 , 4, 3.1, 2, 5])
    [8, 5, 4, 3.1, 2, 1, 0, -15, -15, -15]
    '''
    sortedlst = []
    x = MaxBinaryHeap()
    for i in range(len(numList)):
        x.insert(numList[i])
    while len(x) > 0: 
        sortedlst.append(x.deleteMax())
    return sortedlst

# ============== EXTRA CREDIT
class PriorityQueue:
    '''
        >>> priority_q = PriorityQueue()
        >>> priority_q.isEmpty()
        True
        >>> priority_q.peek()
        >>> priority_q.enqueue('sara',0)
        >>> priority_q
        [(0, 'sara')]
        >>> priority_q.enqueue('kyle',3)
        >>> priority_q
        [(3, 'kyle'), (0, 'sara')]
        >>> priority_q.enqueue('harsh',1)
        >>> priority_q
        [(3, 'kyle'), (0, 'sara'), (1, 'harsh')]
        >>> priority_q.enqueue('ajay',5)
        >>> priority_q
        [(5, 'ajay'), (3, 'kyle'), (1, 'harsh'), (0, 'sara')]
        >>> priority_q.enqueue('daniel',4)
        >>> priority_q.isEmpty()
        False
        >>> priority_q
        [(5, 'ajay'), (4, 'daniel'), (1, 'harsh'), (0, 'sara'), (3, 'kyle')]
        >>> priority_q.enqueue('ryan',7)
        >>> priority_q
        [(7, 'ryan'), (4, 'daniel'), (5, 'ajay'), (0, 'sara'), (3, 'kyle'), (1, 'harsh')]
        >>> priority_q.dequeue()
        'ryan'
        >>> priority_q.peek()
        'ajay'
        >>> priority_q
        [(5, 'ajay'), (4, 'daniel'), (1, 'harsh'), (0, 'sara'), (3, 'kyle')]
        >>> priority_q.dequeue()
        'ajay'
        >>> len(priority_q)
        4
        >>> priority_q.dequeue()
        'daniel'
        >>> priority_q.dequeue()
        'kyle'
        >>> priority_q.dequeue()
        'harsh'
        >>> priority_q.dequeue()
        'sara'
        >>> priority_q.dequeue()
        >>> priority_q.isEmpty()
        True
    '''
    def __init__(self):
        self._items = MaxBinaryHeap()

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    __repr__ = __str__

    def peek(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty():
            return
        return self._items.getMax[1]

    def isEmpty(self):
        if len(self._items) == 0 :
            return True
        return False

    def enqueue(self, value, priority):
        self._items.insert((priority, value))

    def dequeue(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty():
            return None
        return self._items.deleteMax()[1]

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
    # doctest.run_docstring_examples(PriorityQueue, globals(), name='LAB7.py',verbose=True)
