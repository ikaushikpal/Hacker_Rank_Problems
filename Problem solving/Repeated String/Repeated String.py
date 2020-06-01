s = input()
n = int(input())
count = s.count('a')
count *= n//len(s)
for i in range(0,n%len(s)):
    if s[i]=='a':
        count += 1

print(count)