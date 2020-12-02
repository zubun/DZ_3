# a = 3 ** -4
# print(a)
# print(pow(3,-4))


'''Не совсем понял зачем это задание решать через оператор **, поэтому привел только одно решение'''
def my_func (arg_1, arg_2):
    result_1 = 1
    for i in range(abs(arg_2)):
        result_1 *= arg_1
    if arg_2 > 0:
        return result_1
    else:
        return 1 / result_1


arg_1 = int(input("Введите первое число:" ))
arg_2 = int(input("Введите второе число:" ))
result = my_func(arg_1, arg_2)
print(result)




