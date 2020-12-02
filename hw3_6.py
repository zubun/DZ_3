# a = ('фикус ivbrec')
# print(a.title())
# a = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
# for el in range(len(a)):
#     b = a[el]
#     print(ord(b))
# print(ord("adc"))

'''Функция возвращающая первую заглавную букву в слове на латинице'''
def int_func(arg):
    list_1 = list(arg)
    arg_1 = list_1[0]
    arg_2 = ord(arg_1)
    if 97 < arg_2 < 122:
        # arg_1 = list_1[0]
        arg_2 = ord(arg_1)
        arg_3 = chr(arg_2 - 32)
        list_1.pop(0)
        list_1.insert(0,arg_3)
        list_2 = ''.join(list_1)
        return (list_2)
    else:
        return (arg)

'''Функция возвращающая первую заглавную букву в строке слов на латинице'''
def int_func_line(arg_line):
    arg_line_2 = arg_line.split()
    new_line = []
    for line in range(len(arg_line_2)):
        word = arg_line_2[line]
        new_line.append(int_func(word))
    end_line = ' '.join(new_line)
    return end_line
#

words = input("Введите слово:")
lines = input("Введите строку:")
print(int_func(words))
print(int_func_line(lines))







