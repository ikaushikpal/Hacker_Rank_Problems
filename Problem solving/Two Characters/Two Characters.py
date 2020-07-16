from collections import Counter


def twoCharacter(text):
    dic = dict()
    c = Counter(text)
    dic = c.copy()
    dic = dict(c)
    keys = list(dic.keys())
    result = []
    for i in keys:
        for j in keys:
            if i != j:
                s1 = i+j
                s2 = j+i
                if s1 in text or s2 in text:
                    d = abs(c[i]-c[j])
                    if d == 1:
                        value = c[i] + c[j]
                        result.append(value)

    if len(result) == 0:
        print(0)
    else:
        v = Counter(result).most_common(1)
        print(v[0][0])


if __name__ == "__main__":
    n = int(input())
    text = input()
    twoCharacter(text)
