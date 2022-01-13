# Author: MOG 1/13/22

def return_even(lst):
    evens = []
    for i, x in enumerate(lst):
        if i % 2 != 0:
            evens.append(x)
    return evens

print(return_even([1,2,3,4,5,6,7,8]))