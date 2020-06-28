def flippingBits(n):
    bin_equivalent = bin(n)
    bin_equivalent.split('b')
    bin_equivalent = bin_equivalent[2:]

    req_len = 32 - len(bin_equivalent)
    extra_zeros = '0' * req_len
    bin_equivalent = extra_zeros + bin_equivalent
    result = ''

    for i in range(len(bin_equivalent)):
        if bin_equivalent[i] == '0':
            result += '1'
        else:
            result += '0'

    print(int(result, 2))


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        n = int(input())
        flippingBits(n)
