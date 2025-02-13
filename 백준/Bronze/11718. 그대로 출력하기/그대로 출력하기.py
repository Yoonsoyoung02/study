import sys

while True:
    string = sys.stdin.readline()
    if not string:
        break
    sys.stdout.write(string)