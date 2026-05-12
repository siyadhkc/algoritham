def add_binary(a, b):

    i = len(a) - 1
    j = len(b) - 1

    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:

        bit_a = int(a[i]) if i >= 0 else 0
        bit_b = int(b[j]) if j >= 0 else 0

        total = bit_a + bit_b + carry

        result.append(str(total % 2))

        carry = total // 2

        i -= 1
        j -= 1

    return ''.join(result[::-1])


# Example
a = "1011"
b = "1101"

print(add_binary(a, b))



# binary sibstraction 
def subtract_binary(a, b):

    i = len(a) - 1
    j = len(b) - 1

    borrow = 0
    result = []

    while i >= 0:

        bit_a = int(a[i]) - borrow
        bit_b = int(b[j]) if j >= 0 else 0

        if bit_a < bit_b:
            bit_a += 2
            borrow = 1
        else:
            borrow = 0

        result_bit = bit_a - bit_b
        result.append(str(result_bit))

        i -= 1
        j -= 1

    # remove leading zeros
    while len(result) > 1 and result[-1] == '0':
        result.pop()

    return ''.join(result[::-1])


# Example
a = "1101"
b = "101"

print(subtract_binary(a, b))