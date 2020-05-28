def getMoneySpent(keyboards, drives, b):
    keyboard_len = len(keyboards)
    drives_len = len(drives)

    price_list = []

    for i in range(keyboard_len):
        for j in range(drives_len):
            val = drives[j]+keyboards[i]
            if val<=b:
                price_list.append(val)
    if not price_list:
        return -1
    else:
        return max(price_list)



print(getMoneySpent([3, 1],[5, 2 ,8],10))