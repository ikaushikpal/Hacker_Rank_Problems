def marsExploration(s):
    count = 0
    for i in range(len(s)):
        if i%3 == 0 or i%3 == 2:
            if s[i] != 'S':
                count += 1
        elif i%3 == 1 and s[i] !='O':
            count += 1

    return count


print(marsExploration("SOSSOT"))
