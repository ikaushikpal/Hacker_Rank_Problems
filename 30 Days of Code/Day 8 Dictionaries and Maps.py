n = int(input())
values ={}
for _ in range(n):
    key, value = input().split()
    values[key] = value

for _ in range(0,n):
    try:
        quary = input()
        if quary in values:
            print(f"{quary}={values[quary]}")
        else:
            print("Not found")
    except:
        break