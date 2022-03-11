words_list = input("Input words: ")

words_list = words_list.split(',')
words_list.sort()
print('The result is: ')
print((', ').join(words_list))