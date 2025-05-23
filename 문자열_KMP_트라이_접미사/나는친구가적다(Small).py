num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def determine(str1, str2):
    str1_new = ''
    for char in str1:
        if char in num:
            continue
        else:
            str1_new += char
    if str2 in str1_new:
        print ('1')
    else:
        print ('0')

s = input()
k = input()
determine(s, k)