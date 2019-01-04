palindroms = 1
while palindroms < 2019:
    b = palindroms
    c = 0

    while b > 0:
        c = c*10+(b%10)
        b = b // 10
        if c == palindroms:
            print (c)
    palindroms += 1
