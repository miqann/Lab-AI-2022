def dictionary(x):
    begin = '{'
    for i in range (1, x + 1):
        if i != 1:
           begin += ','
        work = ' {i1}:{i2}'.format(i1 = i, i2 = i**2)
        begin += work
    begin += '}'
    return begin

print(dictionary(int(input('Enter n: '))))
    