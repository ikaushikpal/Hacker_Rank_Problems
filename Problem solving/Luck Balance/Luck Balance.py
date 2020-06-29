def luckBalance(k, important_contest, unimportant_contest):
    total_luck = sum(important_contest) + sum(unimportant_contest)
    loses = len(important_contest)-k

    while loses > 0:
        value = min(important_contest)
        total_luck -= 2*value
        important_contest.remove(value)
        loses -= 1

    print(total_luck)


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    contests, important_contest, unimportant_contest = [], [], []

    for _ in range(n):
        contests = list(map(int, input().rstrip().split()))
        if contests[1] == 1:
            important_contest.append(contests[0])
        else:
            unimportant_contest.append(contests[0])

    luckBalance(k, important_contest, unimportant_contest)
