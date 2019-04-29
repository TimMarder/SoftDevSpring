# Tim Marder
# SoftDev2 pd06
# K20 -- Reductio ad Absurdum
# 2019-04-29

from functools import reduce

file = open( 'dracula.txt' , 'r' )
stuff = file.read()
stuff = stuff.split()

def single_freq( word ):
    return reduce(
        (lambda a , b: a + b),
        [ 1 if x.lower() == word.lower() else 0 for x in stuff ]
    )

def total_freq( words ):
    return reduce(
        (lambda a , b: a + b),
        [ 1 if x.lower() in [ y.lower() for y in words ] else 0 for x in stuff ]
    )

def most_freq():
    return reduce(
        (lambda a , b: a if single_freq( a ) > single_freq( b ) else b),
        list( set( [ x.lower() for x in stuff ] ) )
    )

print( single_freq( "how" ) )
print( single_freq( "are" ) )
print( single_freq( "you" ) )

print( total_freq( [ "how" , "are" , "we" ] ) )

print( most_freq() )
