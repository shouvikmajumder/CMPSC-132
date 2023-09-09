# LAB 8
# REMINDER: The work in this assignment must be your own original work and must be completed alone.


# ========= PART 1 ================

vector_plus_one = lambda lst: list(map(lambda x: x+1, lst))    #-- Replace None with your lambda function

collatz_steps =  lambda lst: list(map(lambda n: 3 * n + 1 if n % 2 == 1 else n // 2, filter(lambda x: isinstance(x, int) and x >= 1, lst)))     #-- Replace None with your lambda function

mean =  lambda lst: sum(lst) / len(lst)    #-- Replace None with your lambda function

range_diff = lambda lst: max(lst) - min(lst)     #-- Replace None with your lambda function

std =  lambda lst: ((sum(map(lambda x: (x - mean(lst)) ** 2, lst))) / len(lst)) ** 0.5 #-- Replace None with your lambda function

data_analysis = lambda data, funcs: list(map(lambda f: f(data), funcs))     #-- Replace None with your lambda function

exchange_matrix = lambda n: [[int(i==n-j-1) for i in range(n)] for j in range(n)]     #-- Replace None with your lambda function

matrix_adder =  lambda A, B: [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]     #-- Replace None with your lambda function

get_matrix = lambda s: [list(map(int, row.split())) for row in s.split("\n") if row]     #-- Replace None with your lambda function

# ========= PART 2 ================

def mulDigits(num, fn):
    '''
        >>> isTwo = lambda num: num == 2
        >>> mulDigits(5724892472, isTwo)
        8
        >>> def divByFour(num):
        ...     return not num%4
        ...
        >>> mulDigits(5724892472, divByFour)
        128
        >>> mulDigits(155794, isTwo)
        1
        >>> mulDigits(67945125482222152, isTwo)
        64
        >>> mulDigits(679451254828822152, divByFour)
        8192
    '''
    output = 1
    while num > 0:
        digit = num % 10
        if fn(digit):
            output *= digit
        num //= 10
    return output
    

def getCount(x):
    '''
        >>> getCount(6)(62156)
        2
        >>> digit = getCount(7)
        >>> digit(9457845778457077076)
        7
        >>> digit(-945784578457077076)
        6
        >>> getCount(6)(-65062156)
        3
    '''
    def count(num):
        if num == 0:
            return int(x == 0)
        elif num < 0:
            num = -num
        digit_count = 0
        while num != 0:
            if num % 10 == x:
                digit_count += 1
            num //= 10
        return digit_count
    return count


def itemize(num):
    '''
        >>> gen = itemize(-6125)
        >>> next(gen)
        5
        >>> next(gen)
        2
        >>> next(gen)
        1
        >>> next(gen)
        6
        >>> next(gen)
        Traceback (most recent call last):
        ...
        StopIteration
    '''
    if num == 0:
        yield 0
    elif num < 0:
        num = -num
    while num != 0:
        digit = num % 10
        yield digit
        num //= 10



def frange(*args):
    '''
        >>> list(frange(7.5))
        [0, 1, 2, 3, 4, 5, 6, 7]
        >>> seq = frange(0,7, 0.1)
        >>> type(seq)
        <class 'generator'>
        >>> list(seq)
        [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9]
        >>> list(seq)
        []
        >>> list(frange(0,7, 0.75))
        [0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25, 6.0, 6.75]
        >>> list(frange(0,7.75, 0.75))
        [0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25, 6.0, 6.75, 7.5]
        >>> list(frange(0,7.75, -0.5))
        []
        >>> list(frange(7.75,0, -0.5))
        [7.75, 7.25, 6.75, 6.25, 5.75, 5.25, 4.75, 4.25, 3.75, 3.25, 2.75, 2.25, 1.75, 1.25, 0.75, 0.25]
    '''
    start, step = 0, 1

    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    else:
        raise TypeError(f'frange expected at most 3 arguments, got {len(args)}')
    # - YOUR CODE STARTS HERE
    while (step > 0 and start < stop) or (step < 0 and start > stop):
        yield round(start, 3)
        start += step


def genFib(fn):
    '''
        >>> evens = genFib(lambda x: x % 2 == 0)
        >>> [next(evens) for _ in range(15)]
        [0, 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578, 14930352, 63245986, 267914296]
        >>> seq = genFib(lambda x: x > 20 and x % 2)
        >>> next(seq)
        21
        >>> next(seq)
        55
        >>> next(seq)
        89
        >>> next(seq)
        233
        >>> next(seq)
        377
        >>> next(seq)
        987
        >>> next(seq)
        1597
        >>> next(seq)
        4181

        >>> evens = genFib(lambda x: x % 2 == 0)
        >>> sum([next(evens) for _ in range(50)])
        3080657373857639014791750813074
        >>> odds = genFib(lambda x: x % 2 == 1)
        >>> [next(odds) for i in range(25)]
        [1, 1, 3, 5, 13, 21, 55, 89, 233, 377, 987, 1597, 4181, 6765, 17711, 28657, 75025, 121393, 317811, 514229, 1346269, 2178309, 5702887, 9227465, 24157817]
        >>> ends_with_5 = genFib(lambda x: x % 10 == 5)
        >>> [next(ends_with_5) for i in range(10)]
        [5, 55, 6765, 75025, 9227465, 102334155, 12586269025, 139583862445, 17167680177565, 190392490709135]

    # '''
    first, second = 0, 1
    while True:
        if fn(first):
            yield first
        first, second = second, first + second

# ========= TESTING ASSERTIONS FOR PART 1 - DO NOT MODIFY ================

def test_vector_plus_one():
    assert vector_plus_one([1, 2, 3]) == [2, 3, 4]
    assert vector_plus_one([0, 0, 0]) == [1, 1, 1]
    assert vector_plus_one([-1, -2, -3, -4, -5]) == [0, -1, -2, -3, -4]
    assert vector_plus_one([]) == []
    print('All cases for vector_plus_one passed!')

def test_collatz_steps():
    assert collatz_steps([1, 2, 3, 4]) == [4, 1, 10, 2]
    assert collatz_steps([0, "", -2, 1.5, 2.0]) == []
    assert collatz_steps([-1, -2, -3, -4, -5]) == []
    assert collatz_steps([]) == []
    print('All cases for collatz_steps passed!')

def test_mean():
    assert mean([1, 2, 3]) == 2
    assert mean([0, 0, 0]) == 0
    assert mean([-1, -2, -3, -4, -5]) == -3
    print('All cases for mean passed!')

def test_range_diff():
    assert range_diff([1, 2, 3]) == 2
    assert range_diff([10, 10, 10]) == 0
    assert range_diff([-1, -2, -3, -4, -5]) == 4
    print('All cases for range_diff passed!')

def test_std():
    import math
    assert math.isclose(std([1, 2, 3]), 0.816496580927726)
    assert std([10, 10, 10]) == 0
    assert math.isclose(std([-1, -2, -3, -4, -5]), 1.4142135623730951)
    print('All cases for std passed!')


def test_data_analysis():
    assert data_analysis([1, 2, 3], [min, max]) == [1, 3]
    assert data_analysis([0, 0, 0], [mean, range_diff, std]) == [0, 0, 0]
    assert data_analysis([-1, -2, -3, -4, -5], [mean, range_diff]) == [-3, 4]
    print('All cases for data_analysis passed!')


def test_exchange_matrix():
    assert exchange_matrix(1) == [[1]]
    assert exchange_matrix(2) == [[0, 1], [1, 0]]
    assert exchange_matrix(3) == [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
    print('All cases for exchange_matrix passed!')


def test_matrix_adder():
    assert matrix_adder([[3, 1], [2, 7]], [[4, 2], [5, 7]]) == [[7, 3], [7, 14]]
    assert matrix_adder([[1, 2, 3], [1, 2, 3], [1, 2, 3]], [[4, 5, 6], [4, 5, 6], [4, 5, 6]]) == [[5, 7, 9], [5, 7, 9], [5, 7, 9]]
    assert matrix_adder([[8, 2, -6, 2], [1, 5, 2, 24.5], [34, 4, 4, 2], [5, -98, 1.5, 4]], [[1, 7, 9, 55], [9.5, 45.5, 5, -9], [1, 5, 6, 67], [8, 4, 1, 7]]) == [[9, 9, 3, 57], [10.5, 50.5, 7, 15.5], [35, 9, 10, 69], [13, -94, 2.5, 11]]
    print('All cases for matrix_adder passed!')


def test_get_matrix():
    assert get_matrix("1 2 3") == [[1, 2, 3]]
    assert get_matrix("1 2 3\n\n4 5 6") == [[1, 2, 3], [4, 5, 6]]
    assert get_matrix("1\n2\n3") == [[1], [2], [3]]
    print('All cases for get_matrix passed!')


# ========= STARTER TESTING ================

def run_tests():
    # For Part 1
    # -- Uncomment function per function to test
    # test_vector_plus_one()
    # test_collatz_steps()
    # test_mean()
    # test_range_diff()
    # test_std()
    # test_data_analysis()
    # test_exchange_matrix()
    # test_matrix_adder()
    # test_get_matrix()

    # For Part 2
    import doctest    
    # -- Run tests per function - Uncomment the next line to run doctest by function. Replace mulDigits with the name of the function you want to test
    # doctest.testmod(verbose=True)
    doctest.run_docstring_examples(genFib, globals(), name='LA8',verbose=True)   

if __name__ == "__main__":
    run_tests()

