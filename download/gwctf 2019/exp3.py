flag = ['0x666c61', '0x677b72', '0x655f69', '0x735f67', '0x726561', '0x74217d']
for i in flag:
    temp = i[2:]
    while temp != '':
        print(chr(int('0x' + temp[:2], 16)), end = '')
        temp = temp[2:]
