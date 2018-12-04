"""
prints a sideways triangle like so:
#
##
###
####
###
##
#
"""

# Did this one using a coditional before reading the explanation in the book
for i in range(8):
    if i >= 4:
        for k in range(1, 8 - i):
            print('#', end='')
    else:
        for j in range(0, 1+i):
            print('#', end='')
    print()


# Was able to figure this out after reading the explanation in the book
for i in range(8):
    for j in range(0,4 - abs(4-i)):
        print('#', end='')
    print()
