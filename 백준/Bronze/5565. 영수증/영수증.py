import sys

price_list = []

for i in range (10):
    price = int(sys.stdin.readline().rstrip())

    if i == 0:
        total = price
    else:
        price_list.append(price)
        
sys.stdout.write(f'{total-sum(price_list)}')
