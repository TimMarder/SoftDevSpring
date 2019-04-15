# Tangerines- Alexander Liu, Michelle Tang, Tim Marder
# Softdev2 pd6
# K16 -- Do You Even List?
# 2019-04-12

# 1. ['00', '22', '44', '66', '88']
# 1a
def loopyOne():
    var = 0
    num = []
    while (len(num) < 5):
        num.append( str(var) + str(var) )
        var += 2
    return num

# 1b
def listcompOne():
    nums = "02468"
    array = [x + x for x in nums]
    return array

# 2. [7, 17, 27, 37, 47]
# 2a
def loopyTwo():
    var = 0
    num = [7]
    while (len(num) < 5):
        num.append( 10 + num[len(num) - 1] )
        var += 1
    return num

# 2b
def listcompTwo():
    nums = "01234"
    array = [ int(x + "7") for x in nums]
    return array

# 3. [0, 0, 0, 0, 1, 2, 0, 2, 4]
# 3a
def loopyThree():
    var = 0
    i = 0
    num = [0]
    while (len(num) < 9):
        while (i < 2):
            num.append( num[len(num) - 1] + var )
            i += 1
        num.append(0)
        i = 0
        var += 1
    num.pop()
    return num

# 3b
def listcompThree():
    nums = "012"
    array0 = [ int(x) * 0 for x in nums]
    array1 = [ int(x) * 1 for x in nums]
    array2 = [ int(x) * 2 for x in nums]
    array = array0 + array1 + array2

    return array

# helper function
def primeFinder():
    num = [99]
    next = 0
    i = 0
    while (num[len(num) - 1] > 4):
        next = num[len(num) - 1] - 2
        num.append( next )
        # print(next)
        while (i < len(num)):
            if (num[i] % next == 0):
                num.pop(i)
            i += 1
    num.append( 2 )
    num.append( 1 )
    return num

# 4. Composites on range [0,100], in ascending order.
# 4a
def loopyFour():
    prime = primeFinder()
    num = []
    i = 1
    for a in range( 101 ):
        num.append(i)
        i += 1
    for x in prime:
        num.remove(x)
    return num

# 4b
def listcompFour():
    return [i for i in range(2, 101) if 1 in [1 if i % j == 0 else 0 for j in range(2, i)]]

# 5. Primes on range [0,100], in ascending order.
# 5a
def loopyFive():
    num = primeFinder()
    num.reverse()
    return num

# 5b
def listcompFive():
    return [i for i in range(2, 101) if 1 not in [1 if i % j == 0 else 0 for j in range(2, i)]]

# 6a
def loopySix(n):
    i = 1
    list = []
    while (i < n):
        if not n % i:
            list.append(i)
        i += 1
    list.append(n)
    return list

# 6b
def listcompSix(n):
    list = [i for i in range(n) if i > 0 and n % i == 0]
    list.append(n)
    return list


# 7. transpose matrix

# i = inner list; j = outer list
def transpose_matrix(matrix):
    transpose = []
    for i in range(len(matrix[0])):
        transpose.append([])
        for j in range(len(matrix)):
            transpose[i].append(matrix[j][i])

    return transpose

def transpose_matrix_listcomp(matrix):
    transpose = [ [ matrix[j][i] for j in range(len(matrix)) ] for i in range(len(matrix[0])) ]
    return transpose

print( " 1: ? -> ['00', '22', '44', '66', '88'] ")
print(" 1A: " + str(loopyOne()))
print(" 1B: " + str(listcompOne()))
print ("\n==========================================\n")
print( " 2: ? -> [7, 17, 27, 37, 47] ")
print( " 2A: " + str(loopyTwo()))
print( " 2B: " + str(listcompTwo()))
print ("\n==========================================\n")
print( " 3: ? -> [0, 0, 0, 0, 1, 2, 0, 2, 4] ")
print( " 3A: " + str(loopyThree()))
print( " 3B: " + str(listcompThree()))
print ("\n==========================================\n")
print( " 4: Composites on range [0,100], in ascending order. ")
print( " 4A: " + str(loopyFour()))
print( " 4B: " + str(listcompFour()))
print ("\n==========================================\n")
print( " 5: Primes on range [0,100], in ascending order. ")
print( " 5A: " + str(loopyFive()))
print( " 5B: " + str(listcompFive()))
print ("\n==========================================\n")
print( " 6: All divisors of a number, listed in ascending order. ")
print( " 6A: " + str(loopySix(100)))
print( " 6B: " + str(listcompSix(100)))
print ("\n==========================================\n")
print( " 7: Transpose a matrix (turn rows into columns and vice-versa...). ")
array = [[0, 1], [2, 3], [4, 5]]
mat = transpose_matrix(array)
matLC = transpose_matrix_listcomp(array)
print( " 7A: " + str(mat))
print( " 7B: " + str(matLC))
print ("\n==========================================\n")
