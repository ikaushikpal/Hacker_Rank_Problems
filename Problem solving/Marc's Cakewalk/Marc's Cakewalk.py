def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    total_calories = 0
    for i in range(len(calorie)):
        total_calories += calorie[i] * (2**i)

    return total_calories


if __name__ == '__main__':
    n = int(input())
    calorie = list(map(int, input().rstrip().split()))
    result = marcsCakewalk(calorie)
    print(result)
