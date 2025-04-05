money_list = []
while True:
    money = int(input())
    if money == -1:
        break
    else:
        money_list.append(money)

print(sum(money_list))