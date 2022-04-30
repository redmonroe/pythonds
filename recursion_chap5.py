
num_list = [1,3,5,7,9]
def recursive_sumlist(list1=None):
    if len(list1) <= 1:
        return list1[0]
    else:
        list1.append(list1.pop() + list1.pop(0))
        return recursive_sumlist(list1)


print(recursive_sumlist(list1=num_list))