s = 'abbbbbbbbbbaa'
count = 1
if len(s) != 1:
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            print(s[i-1]+str(count), end='')
            count = 1
    print(s[i] + str(count))
else: print(s+str(count))
