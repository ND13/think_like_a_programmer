"""
prints a half square like this
#####
####
###
##
#
"""

for i in range(5):
    for j in range(0, 5-i):
        print('#', end='')
    print()
