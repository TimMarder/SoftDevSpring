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


print("1A: ")
print(loopyOne())

# 1b
def listcompOne():
    nums = "02468"
    array = [x + x for x in nums]
    return array


print("1B: ")
print(listcompOne())

# 2. [7, 17, 27, 37, 47]
# 2a
def loopyTwo():
    var = 0
    num = [7]
    while (len(num) < 5):
        num.append( 10 + num[len(num) - 1] )
        var += 1
    return num


print("2A: ")
print(loopyTwo())

# 2b
def listcompTwo():
    nums = "01234"
    array = [ int(x + "7") for x in nums]
    return array


print("2B: ")
print(listcompTwo())

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


print("3A: ")
print(loopyThree())

# 3b
def listcompThree():
    nums = "012"
    array0 = [ int(x) * 0 for x in nums]
    array1 = [ int(x) * 1 for x in nums]
    array2 = [ int(x) * 2 for x in nums]
    array = array0 + array1 + array2

    return array


print("3B: ")
print(listcompThree())

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


print("4A: ")
print(loopyFour())

# 4b
def listcompFour():
    nums = "012"
    array0 = [ int(x) * 0 for x in nums]
    array1 = [ int(x) * 1 for x in nums]
    array2 = [ int(x) * 2 for x in nums]
    array = array0 + array1 + array2

    return array


print("4B: ")
print(listcompFour())

# 5. Primes on range [0,100], in ascending order.
# 5a
def loopyFive():
    num = primeFinder()
    num.reverse()
    return num


print("5A: ")
print(loopyFive())

# 5b
def listcompFive():
    nums = "012"
    array0 = [ int(x) * 0 for x in nums]
    array1 = [ int(x) * 1 for x in nums]
    array2 = [ int(x) * 2 for x in nums]
    array = array0 + array1 + array2

    return array


print("5B: ")
print(listcompFive())


# 7. transpose matrix
print("7:: ")

# i = inner list; j = outer list
def transpose_matrix(matrix):
    transpose = []
    for i in range(len(matrix[0])):
        transpose.append([])
        for j in range(len(matrix)):
            transpose[i].append(matrix[j][i])

    return transpose


array = [[0, 1], [2, 3], [4, 5]]
mat = transpose_matrix(array)
print(mat)

def transpose_matrix_listcomp(matrix):
    transpose = [ [ matrix[j][i] for j in range(len(matrix)) ] for i in range(len(matrix[0])) ]
    return transpose


matLC = transpose_matrix_listcomp(array)
print(matLC)
