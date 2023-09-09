# HW3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
import doctest
class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self): 
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        # YOUR CODE STARTS HERE
        if self.top == None:
            return True
        return False

    def __len__(self): 
        # YOUR CODE STARTS HERE
        count = 0
        node = self.top
        while node:
            count+=1
            node = node.next
        return count
            
            

    def push(self,value):
        # YOUR CODE STARTS HERE
        newnode = Node(value)
        newnode.next = self.top
        self.top = newnode
     
    def pop(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty():
            return None
        else:
            poppedNode = self.top
            self.top = self.top.next
            poppedNode.next = None
            return poppedNode.value
        

    def peek(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty():
            return None
        else: return self.top.value



#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None

    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            # print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        # YOUR CODE STARTS HERE
        try:
            float(txt)
            return True
        except ValueError:
            return False


    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack object for expression processing

            >>> x=Calculator()
            >>> x._getPostfix('2 ^ 4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2 * 5.34 + 3 ^ 2 + 1 + 4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( 2.5 )')
            '2.5'
            >>> x._getPostfix('( 2 { 5.0 } )')
            '2.0 5.0 *'
            >>> x._getPostfix(' 5 ( 2 + { 5 + 3.5 } )')
            '5.0 2.0 5.0 3.5 + + *'
            >>> x._getPostfix ('( { 2 } )')
            '2.0'
            >>> x._getPostfix ('2 * ( [ 5 + -3 ] ^ 2 + { 1 + 4 } )')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('[ 2 * ( < 5 + 3 > ^ 2 + ( 1 + 4 ) ) ]')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( { 2 * { { 5 + 3 } ^ 2 + ( 1 + 4 ) } } )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2 * < -5 + 3 > ^ 2 + < 1 + 4 >')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('2 * 5 + 3 ^ - 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ]')
            >>> x._getPostfix(' ( 2 * { 5 + 3 ) ^ 2 + ( 1 + 4 ] }')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ) 1 + 4 (')
            >>> x._getPostfix('2 * 5% + 3 ^ + -2 + 1 + 4')
        '''
        # YOUR CODE STARTS HERE     
        
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression
        pfexpression = []
        operatordict ={"{":-1, "(":-1,"[":-1, "<":-1, "+": 1,"-": 1,"*" : 2 ,"/": 2,"^" : 3}
        ori = txt.split(" ")
        split = []
        bracketdict={")":"(","}":"{", ">":"<", "]": "["}
        c = len(ori)
        it = 0
        while it < c:
            
            if it== c-1:
                split.append(ori[it])
                it+=1
            elif (self._isNumber(ori[it]) and (ori[it+1] in bracketdict.values())):
                split.append(ori[it])
                split.append('*')
                split.append(ori[it+1])
            
                it+=2
            else:
                split.append(ori[it])
                it+=1
        counts = {}
        if split[-1] in "{[(<":
            return
        for element in split:
            if element in counts:
                counts[element] += 1
            else:
                counts[element] = 1
        if '[' not in counts.keys() and ']' in counts.keys():
                return
        if '[' in counts.keys() and ']' in counts.keys():
            if counts['['] != counts[']']:
                return
        if '(' in counts.keys() and ')' in counts.keys():
            if counts['('] != counts[')']:
                return
        c1 = 0
        c2 = 0
        for i in range(len(split)):
            if i <len(split)-1:
                if split[i] in "+/-*^" and split[i+1] in "+/-*^":
                    return 
            if split[i]=='':
                pass
            elif self._isNumber(split[i]) == True:
                pfexpression += [str(float(split[i]))]
                c1+=1
            elif split[i] in "[{(<":   
                postfixStack.push(split[i])
            elif split[i] in operatordict:
                c2+=1
                if postfixStack.isEmpty():
                    postfixStack.push(split[i])
                else:
                    breaking = True
                    while not postfixStack.isEmpty() and breaking:
                        if operatordict[postfixStack.peek()]>=operatordict[split[i]]:
                            pfexpression += [postfixStack.pop()]                        
                        else:
                            breaking = False
                    postfixStack.push(split[i])
            elif split[i] in ")]}>": 
                    if postfixStack.top == bracketdict[split[i]]:
                        postfixStack.pop()
                    else:
                        while postfixStack.peek() != bracketdict[split[i]]:
                            if(bracketdict[split[i]]=="(" and postfixStack.peek()=='['):
                                return

                            pfexpression += [postfixStack.pop()]  
                        postfixStack.pop()       
        if c1-c2!=1:
            return                      
        while not postfixStack.isEmpty():
            if postfixStack.peek() in "<({[":
                return
            pfexpression += [postfixStack.pop()]  

        if split[-1] in "+-/*^":
            return

        return " ".join(pfexpression)
            

    @property
    def calculate(self):
        '''
            calculate must call _getPostfix
            calculate must create and use a Stack object to compute the replaced result as shown in the video lectures
            

            >>> x=Calculator()
            >>> x.setExpr('4 + 3 - 2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 + 3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('4 + 3.65 - 2 / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25 * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr(' 2 - 3 * 4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7 ^ 2 ^ 3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ( [ ( 10 - 2 * 3 ) ] )')
            >>> x.calculate
            12.0
            >>> x.setExpr('8 / 4 * { 3 - 2.45 * [ 4 - 2 ^ 3 ] } + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * [ 4 + 2 * < 5 - 3 ^ 2 > + 1 ] + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 + 3 * ( 2 + { 3.0 } * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * < 4 > ) * [ 2 / 8 + 2 * ( 3 - 1 / 3 ) ] - 2 / 3 ^ 2')
            >>> x.calculate
            1442.7777777777778
            >>> x.setExpr('( 3.5 ) [ 15 ]') 
            >>> x.calculate
            52.5
            >>> x.setExpr('3 { 5 } - 15 + 85 [ 12 ]') 
            >>> x.calculate
            1020.0
            >>> x.setExpr("( -2 / 6 ) + ( 5 { ( 9.4 ) } )") 
            >>> x.calculate
            46.666666666666664
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 + + 3 + 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 + 2")
            >>> x.calculate
            >>> x.setExpr('( ( 2 ) * 10 - 3 * [ 2 - 3 * 2 ) ]')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * ( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( * 10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression
        # YOUR CODE STARTS HERE
        postf= self._getPostfix(self.__expr)
        if postf==None:
            return
        operatorlst = ["^","*","/","+","-"]
        output = 0

        if postf is None:
            return postf 
        else: 
                
            for i in postf.split(" "): 
                if self._isNumber(i):
                    calcStack.push(i)
                else:
                    a = calcStack.pop()
                    b = calcStack.pop()
                    if i in operatorlst and i == "^":
                        output = float(b)**float(a) 
                        calcStack.push(output)
                    elif i in operatorlst and i == "*":
                        output = float(b) * float(a) 
                        calcStack.push(output)
                    elif i in operatorlst and i == "/":
                        if a == 0:
                            return None
                        else:
                            output = float(b) /float(a)
                        calcStack.push(output)
                    elif i in operatorlst and i == "+":
                        output = float(a) + float(b) 
                        calcStack.push(output)
                    elif i in operatorlst and i == "-":
                        output = float(b)- float(a) 
                        calcStack.push(output)
                    elif i not in operatorlst: 
                        return None
            return float(calcStack.pop())
                        
# x = Calculator()
# print(x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4'))
#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 [ x1 - 1 ];x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 [ x1 - 1 ]': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 [ x1 - 1 ]': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * { x1 / 2 };x1 = x2 * 7 / x1;return x1 ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * { x1 / 2 }': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        # YOUR CODE STARTS HERE
        # for i in word[:-1]:
        #     if isinstance(word[-1],int) and i.isalpha() == True:
        #         return True
        #     if i.isalpha() == False:
        #         return False
        # return True
        return  word.isalnum() and word[0].isalpha()
                   

    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 ( x1 - 1 )')
            '7 ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        # YOUR CODE STARTS HERE
        replaced = ''
        splitExp = expr.split()
        for node in splitExp:
            is_Var = self._isVariable(node)
            is_State = (node in self.states.keys())
            if is_Var and is_State:
                replaced = replaced + str(self.states[node]) + ' '
            elif is_Var and not is_State:
                return None
            else:
                replaced = replaced+ node + ' '
        return replaced.strip()

    
            
    def calculateExpressions(self):
        self.states = {} 
        calcObj = Calculator()     
        # YOUR CODE STARTS HERE
        
        calc = {} 
        splitExp = self.expressions.split(';')  
        for line in splitExp:        
            if 'return' in line:
                calcObj.setExpr(self._replaceVariables(line.replace('return', "")))
                calc['_return_'] = calcObj.calculate
            if 'return' not in line: 
                if not self._isVariable(line.split('=')[0].strip()) or self._replaceVariables(line.split('=')[1]) is None: 
                    self.states = {}
                    return None
                else:
                    calcObj.setExpr(self._replaceVariables(line.split('=')[1]))
                    self.states[line.split('=')[0].strip()] = calcObj.calculate 
                    calc[line] = self.states.copy() 
        return calc         
        
            

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
    # doctest.run_docstring_examples(Calculator.calculate, globals(), name='HW3',verbose=True)

