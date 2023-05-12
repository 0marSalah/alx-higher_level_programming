#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    only_2 = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            only_2.append(True)
        else:
            only_2.append(False)
    return only_2
