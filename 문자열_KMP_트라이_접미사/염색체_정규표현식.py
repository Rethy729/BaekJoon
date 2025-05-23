import re

pattern = re.compile(r'^[A-F]?A+F+C+[A-F]?$')

n = int(input())
for _ in range(n):
    chromosome = input()
    if pattern.fullmatch(chromosome):
        print ("Infected!")
    else:
        print ("Good")
