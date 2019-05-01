# Tim Marder
# SoftDev2 pd06
# K22 -- Closure
# 2019=05-01

def repeat(word):
    def repeats(amt):
        return word * amt
    return repeats

r1 = repeat("hello")
r2 = repeat("goodbye")

print( r1(2) )
print( r2(2) )
print( repeat("cool")(3) )

def make_counter():
    x = 0
    def inner():
        nonlocal x
        x += 1
        return x
    def accessor():
        nonlocal x
        return x
    return inner, accessor

crt1 = make_counter()
ctr2 = make_counter()
acc1 = make_counter()

print(ctr1())
print(ctr1())
print(ctr2())
print(ctr1())
print(ctr1())
print(ctr2())
print(ctr2())
print(acc1())
print(acc1())
print(acc1())
