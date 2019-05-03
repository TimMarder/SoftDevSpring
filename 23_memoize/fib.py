# Tim Marder
# SoftDev2 pd06
# K23 --Memoize With Closure
# 2019-05-02

import random

def make_HTML_heading(f):
    txt = f()
    def inner():
        return "<h1>" + txt + "</h1>"
    return inner

@make_HTML_heading
def greet():
    greetings = [ 'Hello', 'Welcome', 'AYO!', 'Hola', 'Bonjour', 'Word up' ]
    return random.choice( greetings )

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

fib1 = memoize(fib)

print( fib1(1) )
print( fib1(3) )
print( fib1(5) )
print( fib1(6) )
print( fib1(8) )
