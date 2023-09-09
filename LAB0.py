def sum_evens(numList):
    """
        >>> sum_evens([1,5,-3,5.5,359,8,14,-25,1000])
        1022.0
        >>> sum_evens([14,5,-3,5,9.0,8,14,7,-846])
        -810.0
        >>> sum_evens([-8.0,-4,1,2,3,4,5,6,12])
        12.0

        To verify output is being returned, not printed
        >>> output = sum_evens([1,5,-3,5,45.5,8.5,-5,500,6.7,-25])
        >>> output
        500.0
    """
    # --- YOU CODE STARTS HERE
    evenlist = []
    counter = 0
    for nums in numList: 
        if nums % 2 ==0:
            evenlist += [nums]
    for evennums in evenlist:
        counter += float(evennums)
    return counter

# print(sum_evens([-8.0,-4,1,2,3,4,5,6,12]))



if __name__ == "__main__":
    import doctest
    # Uncomment the line below if you want to start testing using the examples in the docstring
    doctest.testmod(verbose=True) 
