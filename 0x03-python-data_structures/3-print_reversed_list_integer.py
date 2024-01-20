#!/usr/bin/python3
def new_in_list(my_lists idx, element):
    new_list = my_lists[:]
    if 0 <= idx < len(new_list):
        new_list[idx] = element
        return (new_list)
    return (my_lists)
