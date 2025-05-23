input_str_lst = []
while True:
    line = input()
    if line == 'end':
        break
    input_str_lst.append(line)

mo_eum = ['a', 'e', 'i', 'o', 'u']

def password(pwd):

    count = 0
    for mo in mo_eum:
        if mo not in pwd:
            count += 1
    if count == 5:
        return f'<{pwd}> is not acceptable.'

    binary_str = ''
    for char in pwd:
        if char in mo_eum:
            binary_str += '1'
        else:
            binary_str += '0'
        if len(binary_str)>=3:
            if binary_str[-3:] == '000' or binary_str[-3:] == '111':
                return f'<{pwd}> is not acceptable.'

    for i in range(len(pwd)-1):
        if pwd[i] == pwd[i+1] and (pwd[i] != 'o' and pwd[i] != 'e'):
            return f'<{pwd}> is not acceptable.'

    return f'<{pwd}> is acceptable.'

for pwd in input_str_lst:
    print (password(pwd))