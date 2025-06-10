import sys

def max_camping(l, p, v):
    return (v//p) * l + min(l, v%p)

input = sys.stdin.readline
test_case_lst = []
while True:
    test_case = list(map(int, input().strip().split()))
    if test_case == [0, 0, 0]:
        break
    else:
        test_case_lst.append(test_case)

for i, case in enumerate(test_case_lst):
    l_c, p_c, v_c = case
    print (f'Case {i+1}: {max_camping(l_c, p_c, v_c)}')
