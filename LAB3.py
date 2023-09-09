# LAB 3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# All functions should NOT contain any for/while loops or global variables. Use recursion, otherwise no credit will be given
# You might add a helper functions as long as it is recursive and named helper_<function name as given in this file>



def replace(numList, old, new): 
    """
        >>> input_list = [1, 7, 5.6, 3, 2, 4, 1, 9]
        >>> replace(input_list, 1, 99.9)
        [99.9, 7, 5.6, 3, 2, 4, 99.9, 9]
        >>> input_list
        [1, 7, 5.6, 3, 2, 4, 1, 9]
        >>> replace([1,7, 5.6, 3, 2, 4, 1, 9], 5.6, 777) 
        [1, 7, 777, 3, 2, 4, 1, 9]
        >>> replace([1,7, 5.6, 3, 2, 4, 1, 9], 8, 99)    
        [1, 7, 5.6, 3, 2, 4, 1, 9]
    """
    ## YOUR CODE STARTS HERE
    if len(numList)== 0:
        return []
    if numList[0] == old:
        return [new] + replace(numList[1:], old, new)
    return [numList[0]] + replace(numList[1:], old, new)        

def serial_star(n):
    """
        >>> serial_star(0)
        '*'
        >>> serial_star(3)
        '********'
        >>> serial_star(4)
        '****************'
    """
    ## YOUR CODE STARTS HERE
    if n == 0:
        return "*"
    return serial_star(n-1) + serial_star(n-1)

def get_match(num1, num2):
    """
        >>> get_match(6598, 509)
        1
        >>> get_match(654886625, 115568)
        0
        >>> get_match(654886625, 12880605)
        4
    """
    ## YOUR CODE STARTS HERE
    if num1 == 0 and num2 == 0:
        return 0
    else:
        return (num1 % 10 == num2 % 10) + get_match(num1 // 10, num2 // 10)


def neighbor(num):
    """
        >>> neighbor(24680)
        24680
        >>> neighbor(2222466666678)
        24678
        >>> neighbor(0)
        0
        >>> neighbor(22224666666782)
        246782
        >>> neighbor(2222466666625)
        24625
    """
    ## YOUR CODE STARTS HERE
    if num < 10:
        return num
    elif num % 10 == (num//10) % 10:
        return neighbor(num // 10)
    return neighbor(num // 10) * 10 + num % 10

def run_tests():
    
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace intersection with the name of the function you want to test
    # doctest.run_docstring_examples(neighbor, globals(), name='LAB3',verbose=True)

if __name__ == "__main__":
    run_tests()

