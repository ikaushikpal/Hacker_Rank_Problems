# Hashing approach
# def icecreamParlor(money, arr):
#     maxx_length = max(arr)
#     Hash = [0]*(maxx_length+1)
#     start_value, stop_value = 0, 0

#     for i in range(len(arr)):
#         Hash[arr[i]] += 1

#     for i in range(len(arr)):
#         find = money - arr[i]
#         start_value = i
#         if find == arr[i]:
#             if Hash[find] > 1:
#                 stop_value = i+1
#                 break
#         else:
#             if Hash[find] > 0:
#                 stop_value = arr.index(find)
#                 break

#     print(f"{start_value+1} {stop_value+1}")


def find_value(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i+1

# using array


def icecreamParlor(money, arr):
    temp_arr = [0]*len(arr)
    for i in range(len(arr)):
        temp_arr[i] = arr[i]

    temp_arr.sort()
    i, j = 0, len(arr)-1
    start_value, end_value = 0, 0
    while i <= j:
        start_value = temp_arr[i]
        end_value = temp_arr[j]

        if start_value + end_value == money:
            break
        elif start_value + end_value < money:
            i += 1
        else:
            j -= 1

    if start_value == end_value:
        p1 = find_value(arr, start_value)
        p2 = p1 + 1
    else:
        p1 = find_value(arr, start_value)
        p2 = find_value(arr, end_value)

    if p1 > p2:
        print(f"{p2} {p1}")
    else:
        print(f"{p1} {p2}")


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        m = int(input())
        n = int(input())
        arr = list(map(int, input().rstrip().split()))
        icecreamParlor(m, arr)
