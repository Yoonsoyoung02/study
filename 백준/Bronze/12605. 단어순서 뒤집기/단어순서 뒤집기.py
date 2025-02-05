import sys
N = int(sys.stdin.readline().rstrip())
word = []

for i in range(N):
    word = sys.stdin.readline().rstrip().split()
    reversed_word = word[::-1]
    sys.stdout.write(f"Case #{i+1}: {' '.join(reversed_word)}\n")