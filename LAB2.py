# LAB2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import random
import math

# -------- SECTION 1
class Pantry:
    """"
        >>> sara_pantry = Pantry()
        >>> sara_pantry.stock_pantry('Bread', 2)
        'Pantry Stock for Bread: 2.0'
        >>> sara_pantry.stock_pantry('Cookies', 6)
        'Pantry Stock for Cookies: 6.0'
        >>> sara_pantry.stock_pantry('Chocolate', 4)
        'Pantry Stock for Chocolate: 4.0'
        >>> sara_pantry.stock_pantry('Pasta', 3)
        'Pantry Stock for Pasta: 3.0'
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 6.0, 'Chocolate': 4.0, 'Pasta': 3.0}
        >>> sara_pantry.get_item('Pasta', 2)
        'You have 1.0 of Pasta left'
        >>> sara_pantry.get_item('Pasta', 6)
        'Add Pasta to your shopping list!'
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 6.0, 'Chocolate': 4.0, 'Pasta': 0.0}
        >>> ben_pantry = Pantry()
        >>> ben_pantry.stock_pantry('Cereal', 2)
        'Pantry Stock for Cereal: 2.0'
        >>> ben_pantry.stock_pantry('Noodles', 5)
        'Pantry Stock for Noodles: 5.0'
        >>> ben_pantry.stock_pantry('Cookies', 9)
        'Pantry Stock for Cookies: 9.0'
        >>> ben_pantry.stock_pantry('Cookies', 8)
        'Pantry Stock for Cookies: 17.0'
        >>> ben_pantry.get_item('Pasta', 2)
        "You don't have Pasta"
        >>> ben_pantry.get_item('Cookies', 2.5)
        'You have 14.5 of Cookies left'
        >>> sara_pantry.transfer(ben_pantry, 'Cookies')
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 20.5, 'Chocolate': 4.0, 'Pasta': 0.0}
        >>> ben_pantry.transfer(sara_pantry, 'Rice')
        >>> ben_pantry.transfer(sara_pantry, 'Pasta')
        >>> ben_pantry
        I am a Pantry object, my current stock is {'Cereal': 2.0, 'Noodles': 5.0, 'Cookies': 0.0}
        >>> ben_pantry.transfer(sara_pantry, 'Pasta')
        >>> ben_pantry
        I am a Pantry object, my current stock is {'Cereal': 2.0, 'Noodles': 5.0, 'Cookies': 0.0}
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 20.5, 'Chocolate': 4.0, 'Pasta': 0.0}
    """

    def __init__(self):
        self.items = {}
    
    def __repr__(self):
        #--- YOUR CODE STARTS HERE
        return f"I am a Pantry object, my current stock is {self.items}"

    def stock_pantry(self, item, qty):
        #--- YOUR CODE STARTS HERE
        if item not in self.items:
            self.items[item] = 0 
        if item in self.items:
            self.items[item] += float(qty)
            return f'Pantry Stock for {item}: {float(self.items[item])}'

    def get_item(self, item, qty):
        #--- YOUR CODE STARTS HERE
        if item not in self.items:
            return f"You don't have {item}"
        elif self.items[item]> qty:
            self.items[item] -= float(qty)
            return f'You have {self.items[item]} of {item} left'
        elif self.items[item]<qty:
            self.items[item] = 0.0 
            return f"Add {item} to your shopping list!"
            
    def transfer(self, other_pantry, item):
        #--- YOUR CODE STARTS HERE 
        if item in other_pantry.items:
            if item in self.items and other_pantry.items[item]>0:
                self.items[item] += other_pantry.items[item]
                other_pantry.items[item] = 0.0 
            elif item not in self.items and other_pantry.items[item]>0:
                self.items[item] = other_pantry.items[item]
                other_pantry.items[item] = 0.0
            

# -------- SECTION 2
class Vendor:

    def __init__(self, name):
        '''
            In this class, self refers to Vendor objects
            
            name: str
            vendor_id: random int in the range (999, 999999)
        '''
        self.name = name
        self.vendor_id = random.randint(999, 999999)
    
    def install(self):
        '''
            Creates and initializes (instantiate) an instance of VendingMachine 
        '''
        return VendingMachine()
    
    def restock(self, machine, item, amount):
        '''
            machine: VendingMachine
            item: int
            amount : int/float

            Call _restock for the given VendingMachine object
        '''
        return machine._restock(item, amount)
        


class VendingMachine:
    '''
        In this class, self refers to VendingMachine objects

        >>> john_vendor = Vendor('John Doe')
        >>> west_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> john_vendor.restock(west_machine, 215, 9)
        'Invalid item'
        >>> west_machine.isStocked
        True
        >>> john_vendor.restock(west_machine,156, 1)
        'Current item stock: 4'
        >>> west_machine.getStock
        {156: [1.5, 4], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Please deposit $1.5'
        >>> west_machine.purchase(156,2)
        'Please deposit $3.0'
        >>> west_machine.purchase(156,23)
        'Current 156 stock: 4, try again'
        >>> west_machine.deposit(3)
        'Balance: $3.0'
        >>> west_machine.purchase(156,3)
        'Please deposit $1.5'
        >>> west_machine.purchase(156)
        'Item dispensed, take your $1.5 back'
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.deposit(300)
        'Balance: $300.0'
        >>> west_machine.purchase(876)
        'Invalid item'
        >>> west_machine.purchase(384,3)
        'Item dispensed, take your $292.5 back'
        >>> west_machine.purchase(156,10)
        'Current 156 stock: 3, try again'
        >>> west_machine.purchase(156,3)
        'Please deposit $4.5'
        >>> west_machine.deposit(4.5)
        'Balance: $4.5'
        >>> west_machine.purchase(156,3)
        'Item dispensed'
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 3], 384: [2.5, 0], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Item out of stock'
        >>> west_machine.deposit(6)
        'Balance: $6.0'
        >>> west_machine.purchase(254,3)
        'Item dispensed'
        >>> west_machine.deposit(9)
        'Balance: $9.0'
        >>> west_machine.purchase(879,3)
        'Item dispensed'
        >>> west_machine.isStocked
        False
        >>> west_machine.deposit(5)
        'Machine out of stock. Take your $5.0 back'
        >>> west_machine.purchase(156,2)
        'Machine out of stock'
        >>> west_machine.purchase(665,2)
        'Invalid item'
        >>> east_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 0], 384: [2.5, 0], 879: [3.0, 0]}
        >>> east_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> east_machine.deposit(10)
        'Balance: $10.0'
        >>> east_machine.cancelTransaction()
        'Take your $10.0 back'
        >>> east_machine.purchase(156)
        'Please deposit $1.5'
        >>> east_machine.cancelTransaction()
    '''

    def __init__(self):
        #--- YOUR CODE STARTS HERE
        self.vend = {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        self.balance = 0

    def purchase(self, item, qty=1):
        #--- YOUR CODE STARTS HERE
        if item not in self.vend:
            return "Invalid item"
        if self.isStocked == False:
            return "Machine out of stock"
        if self.vend[item][1] == 0:
            return "Item out of stock"
        if self.vend[item][1] < qty:
            return f'Current {item} stock: {self.vend[item][1]}, try again'
        if self.vend[item][0] * qty > self.balance:
            return f"Please deposit ${float((qty *self.vend[item][0])-self.balance)}"
        if self.vend[item][0] * qty == self.balance:
            self.balance -= qty * self.vend[item][0]
            self.vend[item][1] -= qty
            return "Item dispensed"
        if self.vend[item][0]* qty <self.balance:
            temp = self.balance
            self.balance= 0
            self.vend[item][1] -= qty
            return f"Item dispensed, take your ${(temp-(qty*(self.vend[item][0])))} back"    

    def deposit(self, amount):
        #--- YOUR CODE STARTS HERE
        if self.isStocked == True:
            self.balance += amount 
            return f'Balance: ${float(self.balance)}'
        elif self.isStocked == False:
            return f"Machine out of stock. Take your ${float(amount)} back"


    def _restock(self, item, stock):
        #--- YOUR CODE STARTS HERE
        if item not in self.vend:
            return "Invalid item"
        elif item in self.vend:
            self.vend[item][1] += stock        
            return f"Current item stock: {self.vend[item][1]}"

    @property        
    def isStocked(self):
    #--- YOUR CODE STARTS HERE
        for key in self.vend:
            if self.vend[key][1] >0:
                return True
        return False 
    @property
    def getStock(self):
    #--- YOUR CODE STARTS HERE
        return self.vend

    def cancelTransaction(self):
        #--- YOUR CODE STARTS HERE
        if self.balance == 0:
            return None
        else:
            temp = self.balance 
            self.balance = 0
            return f"Take your ${float(temp)} back" 




# -------- SECTION 3--------#

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line: 
    ''' 
        >>> p1 = Point2D(-7, -9)     
        >>> p2 = Point2D(1, 5.6)
        >>> line1 = Line(p1, p2)
        >>> line1.getDistance
        16.648
        >>> line1.getSlope
        1.825
        >>> line1
        y = 1.825x + 3.775
        >>> line2 = line1*4
        >>> line2.getDistance
        66.592
        >>> line2.getSlope
        1.825
        >>> line2
        y = 1.825x + 15.1
        >>> line1
        y = 1.825x + 3.775
        >>> line3 = line1*4
        >>> line3
        y = 1.825x + 15.1
        >>> line1==line2
        False
        >>> line3==line2
        True
        >>> line5=Line(Point2D(6,48),Point2D(9,21))
        >>> line5
        y = -9.0x + 102.0
        >>> Point2D(45,3) in line5
        False
        >>> Point2D(34,-204) in line5
        True
        >>> line5==9
        False
        >>> line6=Line(Point2D(2,6), Point2D(2,3))
        >>> line6.getDistance
        3.0
        >>> line6.getSlope
        inf
        >>> isinstance(line6.getSlope, float)
        True
        >>> line6
        Undefined
        >>> line7=Line(Point2D(6,5), Point2D(9,5))
        >>> line7.getSlope
        0.0
        >>> line7
        y = 5.0
        >>> Point2D(9,5) in line7
        True
        >>> Point2D(89,5) in line7
        True
        >>> Point2D(12,8) in line7
        False
        >>> (9,5) in line7
        False
    '''

    def __init__(self, point1, point2):
        #--- YOUR CODE STARTS HERE
        self.point1 = point1
        self.point2 = point2

    #--- YOUR CODE STARTS HERE
    @property
    def getDistance(self):
        return round((((self.point1.x - self.point2.x)**2)+((self.point1.y - self.point2.y)**2))**(1/2),3)

    @property
    #--- YOUR CODE STARTS HERE
    def getSlope(self):
        if self.point1.x == self.point2.x: 
            return float('Infinity') 
        if self.point1.x != self.point2.x:
            return round((self.point2.y - self.point1.y)/(self.point2.x-self.point1.x),3) 

    #--- YOUR CODE CONTINUES HERE
    def __repr__(self):
        #--- YOUR CODE STARTS HERE
        b = round((self.point1.y - (self.getSlope * self.point1.x)),3)
        if self.point1.x == self.point2.x:
            return "Undefined"
        elif self.getSlope!=0:
            if b>0:
                return f"y = {self.getSlope}x + {b}"   
            if b==0:
                return f"y = {self.getSlope}x"
            if b<0:
                return f"y = {self.getSlope}x {b}"
        elif self.getSlope == 0:
            return f"y = {b}"
        else:
            return None 

    def __eq__(self,other):
        if isinstance(other,Line):
            if (self.point1.x) == (other.point1.x) and (self.point1.y) == (other.point1.y):
                if (self.point2.x) == (other.point2.x) and (self.point2.y) == (other.point2.y):
                    return True
        return False 
    
    def __mul__ (self, x):
        if not isinstance(x,int):
            return None         
        if isinstance(x,int):
            point1_x = self.point1.x * x
            point1_y = self.point1.y * x 
            point2_x = self.point2.x * x
            point2_y = self.point2.y * x
            p1 = Point2D(point1_x, point1_y)     
            p2 = Point2D(point2_x, point2_y)
            line1 = Line(p1, p2)
        return line1
        # round((point2_y- point1_y)/(point2_x-point1_x),3)


    def __contains__(self,other):
        if isinstance(other,Point2D):
            if math.isclose(other.y,self.getSlope * other.x + (self.point1.y - (self.getSlope * self.point1.x))):
                return True
        return False



def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace intersection with the name of the function you want to test
    # doctest.run_docstring_examples(Line, globals(), name='LAB2',verbose=True)
    
if __name__ == "__main__":
    run_tests()

