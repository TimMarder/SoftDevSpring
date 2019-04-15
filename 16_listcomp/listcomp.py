# Team Liders -- Alex Liu & Tim Marder
# Softdev2 pd6
# K#16 -- Do You Even List?
# 2019-04-12

import math

# classwork stuffs
nums = []
print([x for x in range(8)])
print([x * x for x in range(8)])

p = "myNoobPass1234"

print([x for x in p])   # just prints p
print([x for x in "1234"])  # just prints 1234

UC_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print([x for x in p if x in UC_LETTERS])    # only NP are in both
print([1 for x in p if x in UC_LETTERS])    # prints 1 instead of the value of NP
print([1 if x in UC_LETTERS else 0 for x in p]) # prints 1 for NP but 0 for rest

# assignment

alphaUp, nums, alphaNum = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "0123456789", ".?!&#,;:-_*"
alphaDown = alphaUp.lower()

def minT(password):
    lower = [1 for x in password if x in alphaDown]
    upper = [1 for x in password if x in alphaUp]
    num = [1 for x in password if x in nums]
    return len(upper) > 0 and len(lower) > 0 and len(num) > 0

def strenT(password):
    strength = 0
    lower = [1 for x in password if x in alphaDown]
    upper = [1 for x in password if x in alphaUp]
    num = [1 for x in password if x in nums]
    other = [1 for x in password if x in alphaNum]
    if (len(lower) < 9):
        strength += 0.5
    else:
        strength += 2

    if (len(upper) < 2):
        strength += 0.5
    elif (len(upper) < 4):
        strength += 1
    else:
        strength += 2

    if (len(num) < 2):
        strength += 0.5
    elif (len(num) < 4):
        strength += 1.5
    else:
        strength += 3

    if (len(other) < 1):
        strength += 0
    elif (len(other) < 2):
        strength += 1.5
    else:
        strength += 3
    return (int(math.floor(strength)))


print (minT("password"))
print (minT("saadfghAS12"))
print (strenT("hi"))
print (strenT("saadfghAS12"))
print (strenT("DKFS!@WEsd########lfnd1200000vfghnjkkjgtfdertyujkio345432`!?0"))
