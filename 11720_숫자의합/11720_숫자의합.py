n = input()
m = input()

def num_sum(str):
    sum = 0
    for num in str:
        sum += int(num)
    return sum

print (num_sum(m))