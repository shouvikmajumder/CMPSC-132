# HW1
# REMINDER: The work in this assignment must be your own original work and must be completed alone.


def rectangle(perimeter,area):
    """
        >>> rectangle(14, 10)
        5
        >>> rectangle(12, 5)
        5
        >>> rectangle(25, 25)
        False
        >>> rectangle(50, 100)
        20
        >>> rectangle(11, 5)
        False
        >>> rectangle(11, 4)
        False
    """
    #- YOUR CODE STARTS HERE
    if perimeter == area:
        return False
    for i in range(1,area+1):
        if perimeter == (2*i) + 2*(area/i) :
            return int(area/i)
    return False
        
# print(rectangle(14, 10))

        
def get_index(num, digit):
    """
        >>> get_index(1495, 5)
        1
        >>> get_index(1495, 1)
        4
        >>> get_index(1495423, 4)
        3
        >>> get_index(1495, 7)
        -1
    """
    #- YOUR CODE STARTS HERE
    count =1
    while num != digit: 
        if num % 10 == digit:
            return count
        else:
            count += 1
            num //= 10
        if num == 0:
            return -1
    return count  

def unique_largest(num):
    """
        >>> unique_largest(123132)
        False
        >>> unique_largest(7264578364)
        True
        >>> unique_largest(2)
        True
        >>> unique_largest(444444)
        False
    """
    #- YOUR CODE STARTS HERE
    digit = 0 
    count = 0 
    while num != 0:
        if digit == num %10:
            count +=1
        if digit < num % 10:
            digit = num % 10 #digit is now the highest number 
        num //=10 
    if count == 0:
        return True 
    return False

        



def joined_list(n):
    """
        >>> joined_list(5) 
        [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
        >>> joined_list(-8)     
        [-8, -7, -6, -5, -4, -3, -2, -1, -1, -2, -3, -4, -5, -6, -7, -8]
    """
    #- YOUR CODE STARTS HERE
    newlist = []
    jlist = []
    comblist = []
    if n>0:
        for i in range(1,n+1):
            newlist += [i]
        index = len(newlist)
        while index>0:
            index -= 1 
            jlist += [newlist[index]]
        comblist += newlist + jlist 
        return comblist
    if n<0:
        for i in range(n,0):
            newlist += [i]
        index = len(newlist)
        while index>0:
            index -= 1 
            jlist += [newlist[index]]
        comblist += newlist + jlist 
        return comblist



def hailstone(num):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    #- YOUR CODE STARTS HERE
    newlist = [num]
    if num == 1:
        return newlist
    while num != 1:
        if num %2 == 0:
            num = num/2
            newlist += [int(num)]
        else:
            num = 3 * num + 1
            newlist += [int(num)]
        if num == 1:
            return newlist



def is_isomorphic(word1, word2):
    """
        >>> is_isomorphic("egg", "add")
        True
        >>> is_isomorphic ("foo", "car") 
        False
        >>> is_isomorphic ("badc", "baba") 
        False
    """
    #- YOUR CODE STARTS HERE
    newdict = {}
    newdict2= {}
    newdict3 ={}
    valuelist= []
    check = ""
    index = 0
    for letter in word2:
        valuelist += [letter]
    for letter in word1:
        newdict[letter] = 0
    for key in newdict:
        if newdict[key] == 0:
            newdict[key] = valuelist[index]
            index += 1
    for key in newdict:
        newdict2[newdict[key]] = key
    for key in newdict2:
        newdict3[newdict2[key]] = key 
    for letter in word1:
        if letter in newdict3:
            check += newdict3[letter]
    if check == word2:
        return True
    return False

# print(is_isomorphic("badc", "baba"))
    
def translate(translation_file, msg):
    """
        >>> translate('abbreviations.txt', 'c u in 5.')
        'see you in 5.'
        >>> translate('abbreviations.txt', 'gr8, cu')
        'great, see you'
        >>> translate('abbreviations.txt', 'b4 lunch, luv u!')
        'before lunch, love you!'
    """
    # Open file and read lines into one string all the way to the end of the file
    newlist = []
    tdict= {}
    punctlist = [".","?","!",",",";",":"]   
    newphrase = []
    with open(translation_file) as file:   
        contents = file.read()
    for words in contents.split("\n"):
        newlist+=[words.split("=")]
    for value in newlist: 
        tdict[value[0]] = value[1]
    # translation part
    for phrases in msg.split(" "):
        if phrases[-1] in punctlist:
            if phrases[:-1] in tdict:
                newphrase += [tdict[phrases[:-1]] + phrases[-1]]
            else:
                newphrase += [phrases]
        elif phrases in tdict:
            newphrase += [tdict[phrases]]
        else:
            newphrase += [phrases]
    return " ".join(newphrase)



def addToTrie(trie, word):
    """      
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 
        >>> addToTrie(trie_dict, 'art')
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}}
        >>> addToTrie(trie_dict, 'moon') 
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}, 'm': {'o': {'o': {'n': {'word': True}}}}}
    """
    start = None 
    for letter in word:
        if start == None and letter in trie:
            start = trie[letter]
        elif start == None and letter not in trie:
            trie[letter] = {}
            start = trie[letter]
        elif letter not in start: 
            start[letter] = {}
            start = start[letter]
        elif letter in start:
            start = start[letter]
    start["word"] = True 

def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace rectangle with the name of the function you want to test
    # doctest.run_docstring_examples(addToTrie, globals(), name='HW1',verbose=True)   

if __name__ == "__main__":
    run_tests()

