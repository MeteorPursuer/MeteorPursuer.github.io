enc = "fmesh{umkc_vlrn_glh}"
flag = ''
for i in enc:
    j = ord(i) + 1
    if j < ord('a') or j > ord('l'):
        if j > ord('n') and j <= ord('z'):
            flag += chr(j)
        else:
            flag += i
        continue
    flag += chr(ord(i) - 2)
print(flag)
