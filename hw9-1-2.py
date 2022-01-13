# Author: MOG 1/13/22

def odd_numb(lst):
    odd_numbers = []
    for i, x in enumerate(lst):
        if x % 2 != 0:
            odd_numbers.append([i,x])
    return odd_numbers

print(odd_numb([5,23,7,5,84,1]))