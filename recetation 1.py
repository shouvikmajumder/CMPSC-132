# Recitation Activity 1

def translate(translation, msg):
    """
        >>> translate({'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left', '1':'2'} , '1 UP 2 down left right forward')
        '2 down 2 up right left forward'
        >>> translate({'a':'b', 'candy':'three cookies'}, 'We are in a house of CANDY')
        'we are in b house of three cookies'
    """     
    # -- YOUR CODE STARTS HERE
    temp = msg.lower().split()
    newlist = []
    for words in temp: 
        if words in translation:
            newlist += [translation[words]]
        else: 
            newlist +=[words]
    return " ".join(newlist)





if __name__ == "__main__":
    import doctest
    doctest.testmod()