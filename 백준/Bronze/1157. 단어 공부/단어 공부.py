from collections import Counter

str = input().strip().upper()

res = Counter(str).most_common()

if len(res) > 1 and res[0][1] == res[1][1]:
    print('?')
else:
    print(res[0][0])






