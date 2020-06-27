# def separateNumbers(s):
#     s = str(s)
#     length = len(s)
#     s_rev = s[::-1]
#     i = 1
#     flag = 0
#     while(2*i<length):
#         if abs(int(s_rev[0])-int(s_rev[i])) == 1:
#             if abs(int(s_rev[i])-int(s_rev[2*i])) == 1:
#                 flag = 1
#                 count = i
#                 break
#         i += 1
#     if flag==0:
#         return 'NO'
#     i = 1
#     count_temp = count
#     while i<(length//count):
#         count_temp += count
#         if abs(int(s[0:count])-int(s[count_temp-count:count_temp])) != i:
#             return 'NO'
#         i += 1
#     return f"YES {s[0:count]}"


# def separateNumbers(s):
#     length = len(s)
#     base_str = ''
#     test_value = ''
#     flag = 0

#     for j in range(1, (length//2)+1):
#         base_str = s[0:j]
#         base_value = int(base_str)
#         test_value = base_str
#         i = 1

#         while True:
#             if len(test_value) == length:
#                 break
#             test_value += str(base_value+i)
#             i += 1

#         if test_value == s:
#             flag = 1
#             break

#     if flag == 0:
#         print('NO')
#     else:
#         print(f"YES {base_value}")


# separateNumbers("7")
# separateNumbers("13")
# separateNumbers("91011")
# separateNumbers("1234")
# separateNumbers("99100")
# separateNumbers("101103")


def separateNumbers(s):
    if s[0] == '0':
        print('NO')
        return
    length = len(s)
    test_value = ''
    flag = 0

    for j in range(1, (length//2)+1):
        base_str = s[:j]
        base_value = int(base_str)
        test_value = base_str
        i = 1

        while True:
            if len(test_value) == length:
                break
            test_value += str(base_value+i)
            i += 1

        if test_value == s:
            flag = 1
            break

    if flag == 0:
        print('NO')
    else:
        print(f"YES {base_value}")


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        separateNumbers(s)
