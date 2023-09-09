# LAB1
# REMINDER: The work in this assignment must be your own original work and must be completed alone

def intersection(d1, d2):
    """
        >>> intersection({'a':5, 'b':7, 'd':5},{'d':5, 'a':5, 'b':9, 'c':12}) 
        {'a': 5, 'd': 5}
        >>> intersection({'a':5, 'b':7, 'd':5},{'d':8, 'a':51, 'b':9, 'c':12}) 
        {}
        >>> dict_one = {'a':5, 'b':7, 'd':5, 'c':'32', 'art':35.6}
        >>> dict_two = {'d':8, 'a':51, 'b':9, 'c':'32'}
        >>> intersection(dict_one, dict_two) 
        {'c': '32'}
        >>> dict_one
        {'a': 5, 'b': 7, 'd': 5, 'c': '32', 'art': 35.6}
        >>> dict_two
        {'d': 8, 'a': 51, 'b': 9, 'c': '32'}
    """
    # - YOUR CODE STARTS HERE -
    Similardict= {}
    for keys in d1:
        if keys in d2 and d1[keys] == d2[keys]:
            Similardict[keys] = d1[keys]
    return Similardict

def frequency(d):
    """
        >>> frequency({'a':2, 'b': 2, 'c':1, 'd':1, 'e': 5, 'f': 1}) 
        1
        >>> frequency({'a':2, 'b': 2, 'c':1, 'd':1})                 
        2
        >>> frequency({'a':2, 'b': 2, 'c':1, 'd':1, 'h': 2, 't': 6, 'rr': 6, 'rws':6})   
        2
        >>> frequency({'a':2, 'b': 2, 'c':1, 'd':1, 'h': 2, 't': 6, 'rr': 6, 'rws':6, 'ret': 6, 'z': 5}) 
        6
    """
    # - YOUR CODE STARTS HERE -
    value_frequency= {}
    for key in d: 
        value_frequency[d[key]] = 0
    for key in d: 
        if d[key] in value_frequency:
            value_frequency[d[key]] += 1 
    count = 0 
    trackkey = 0
    for key in value_frequency:
        if value_frequency[key] > count:
            trackkey = key 
            count = value_frequency[key]
    return trackkey

def invert(d):
    """
        >>> invert({'one':1, 'two':2,  'three':3, 'four':4})
        {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
        >>> invert({'one':1, 'two':2, 'uno':1, 'dos':2, 'three':3, 'un':1})
        {3: 'three'}
        >>> invert({'123-456-78':'Sara', '987-12-585':'Alex', '258715':'sara', '00000':'Alex'}) 
        {'Sara': '123-456-78', 'sara': '258715'}
    """
    # - YOUR CODE STARTS HERE -
    outputdict = {}
    valuelist = []
    for key in d:
        value = d[key]
        if value in outputdict:
            del outputdict[d[key]]
            valuelist+= [value]
        elif value not in valuelist: 
            outputdict[d[key]] = key 
    return outputdict

def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace intersection with the name of the function you want to test
    # doctest.run_docstring_examples(invert, globals(), name='LAB1',verbose=True)   

if __name__ == "__main__":
    run_tests()

