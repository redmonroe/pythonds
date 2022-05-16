
num_list = [1,3,5,7,9]
def recursive_sumlist(list1=None):
    breakpoint()
    if len(list1) <= 1:
        return list1[0]
    else:
        return list1[0] + recursive_sumlist(list1[1:])


print(recursive_sumlist(list1=num_list))