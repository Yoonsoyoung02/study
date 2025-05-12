def d(n):
    return n + sum(map(int, str(n)))

generated = set()
for i in range(1, 10001):
    generated.add(d(i))

for i in range(1, 10001):
    if i not in generated:
        print(i)
