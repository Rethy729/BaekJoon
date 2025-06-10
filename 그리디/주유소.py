import sys

def minimum_price(city_num, city_distance, oil_price):
    price = 0
    city_index = 0

    present_oil_price = oil_price[0]
    while city_index < city_num-1:
        if present_oil_price <= oil_price[city_index+1]:
            price += present_oil_price * city_distance[city_index]
            city_index += 1
        elif present_oil_price > oil_price[city_index+1]:
            price += present_oil_price * city_distance[city_index]
            present_oil_price = oil_price[city_index+1]
            city_index += 1
    return price

input = sys.stdin.readline
n = int(input())
distance = list(map(int, input().strip().split()))
price = list(map(int, input().strip().split()))

print (minimum_price(n, distance, price))