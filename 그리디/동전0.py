def min_coins(n, coins_lst, price):

    coin_count = 0
    for i in range(n):
        if coins_lst[n-1-i] > price:
            continue
        else:
            coin_temp = price // coins_lst[n-1-i]
            coin_count += coin_temp
            price = price % coins_lst[n-1-i]

    return coin_count

n, m = map(int, input().strip().split())
coins = []
for i in range(n):
    coins.append(int(input()))

print (min_coins(n, coins, m))