HW_SOURCE_FILE = __file__


def summation(n, term):
    """Return the sum of numbers 1 through n (including n) wíth term applied to each number.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    if n > 1:
        return term(n) + summation(n-1,term)
    else:
        return term(n)

def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    path = [[1]*n for _ in range(m)]

    for i in range(1,m):
        for j in range(1,n):
            path[i][j] = path[i-1][j] + path[i][j-1]

    return path[m-1][n-1]

def pascal(row, column):
    """Returns the value of the item in Pascal's Triangle
    whose position is specified by row and column.
    >>> pascal(0, 0)    # The top left (the point of the triangle)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 3 (1 3 3 1), Column 2
    3
    >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
    6
    """
    if column > row:
        return 0
    pascall = []
    for i in range(1,row+2):
        list_temp = []
        for j in range(1,i+1):
            list_temp.append(1)
        pascall.append(list_temp)

    #print(pascall)
    for i in range(2, row+1):
        for j in range(1, i):
            pascall[i][j] = pascall[i-1][j] + pascall[i-1][j-1]

    return pascall[row][column]




def double_eights(n):
    """ Returns whether or not n has two digits in row that
    are the number 8. Assume n has at least two digits in it.

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'double_eights', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def check(n, flag=0):
        if n == 0:
            return False
        num = n % 10
        if num == 8 and flag == 1:
            return True
        elif num == 8 and flag == 0:
            flag == 1    
            return check(n//10, 1)
    
        return check(n//10, 0)
    
    return check(n)
    
    


