n = input('Enter strings: ')
getString = ''

for i in range(len(n)):
    if (n[i] >= 'a' and n[i] <= 'z'):
        getString = getString + chr((ord(n[i]) - 32))
    else:
        getString = getString + n[i]

print('\n Original words: ', n)
print('\n Result: ', getString)