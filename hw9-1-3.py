# Author: MOG 1/13/22

def find_thing(lst, parser):
    index = -1
    for i, x in enumerate(lst):
        if x == parser:
            index = i
            break
    return index

print(find_thing([1,2,3,4,5,6,7,8,7],7))