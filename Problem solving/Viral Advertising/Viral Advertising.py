from math import floor


def viralAdvertising(n):
    # Day Shared Liked Cumulative
    shared = 5
    liked, cumulative = 0, 0
    for day in range(1, n+1):
        liked = floor(shared/2)
        cumulative += liked
        shared = floor(shared/2)*3

    return cumulative


print(viralAdvertising(5))
