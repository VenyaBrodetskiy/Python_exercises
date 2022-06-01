book = 'a aa abC aa ac abc bcd a'
# book = 'a A a'
book = book.lower().split()
d = {}
for word in book:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
for key in d:
    print(key, ' ', d[key])book