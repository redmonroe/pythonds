from chapter4_basic_ds import Stack
# from chapter4_basic_ds import decimal_to_binary

def decimal_to_binary(dec_number=None):
    s = Stack()
    while dec_number > 0:
        check = dec_number % 2
        s.push(check)
        dec_number = dec_number // 2

    binary_string = []
    for i in range(len(s.items)):
        item = s.items.pop()
        binary_string.append(str(item))

    return ''.join(binary_string)
    
bin45 = decimal_to_binary(dec_number=45)
assert str(bin(45)) == '0b' + str(bin45)
bin45 = decimal_to_binary(dec_number=17)
assert str(bin(17)) == '0b' + str(bin45)
bin45 = decimal_to_binary(dec_number=96)
assert str(bin(96)) == '0b' + str(bin45)