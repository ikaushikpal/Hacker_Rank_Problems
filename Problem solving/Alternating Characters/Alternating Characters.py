def alternatingCharacters(s):
    if len(set(s)) == 1:
        return len(s)-1
    count = 0
    s1 = s.count('AB')
    s2 = s.count('BA')
    if s1 == len(s) // 2 or s2 == len(s) // 2:
        return 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1

    return count


print(alternatingCharacters("AAAA"))
print(alternatingCharacters("BBBBB"))
print(alternatingCharacters("ABABABAB"))
print(alternatingCharacters("BABABA"))
print(alternatingCharacters("AAABBB"))
print(alternatingCharacters("AABAAB"))
