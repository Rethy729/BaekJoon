def check_same(word_1, word_2):
    for i in range(min(len(word_1), len(word_2))):
        if word_1[i] != word_2[i]:
            return False
    return True

def check_consistency(lst):
    for i in range(len(lst)-1):
            if check_same(lst[i], lst[i+1]):
                return False
    return True

total_case = []
n = int(input())
for _ in range(n):
    m = int(input())
    test_case = []
    for _ in range(m):
        num = input()
        test_case.append(num)
    test_case.sort()            #sort 해서 사전순으로 나열한 전화번호 -> i번째와 i+1번째만 비교하면 됨
    total_case.append(test_case)

for case in total_case:
    if check_consistency(case):
        print ("YES")
    else:
        print ("NO")