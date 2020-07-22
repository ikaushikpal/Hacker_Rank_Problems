t1 = list(map(int, input().split()))
t2 = list(map(int, input().split()))
l = len(t1)


# year checking
if(t1[2] > t2[2]):
    print(10000)

# moth and year checking
elif t1[1] > t2[1] and t1[2] >= t2[2]:
    print(f"{500*(t1[1]-t2[1])}")

# date, moth and year checking
elif t1[0] > t2[0] and t1[1] >= t2[1] and t1[2] >= t2[2]:
    print(f"{15*(t1[0]-t2[0])}")

else:
    print(0)
