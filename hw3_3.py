
def my_func (arg_1, arg_2, arg_3):
    '''adding two maximum numbers - сложение двух максимальных чисел'''
    list_1 = [arg_1, arg_2, arg_3]
    number_1 = max(list_1)
    list_1.pop(list_1.index(max(list_1)))
    number_2 = max(list_1)
    summ = number_1 + number_2
    return summ
arg_1 = float(input("Введите первое число:" ))
arg_2 = float(input("Введите второе число:" ))
arg_3 = float(input("Введите третье число:" ))

result = my_func(arg_1, arg_2, arg_3)
print(f"Сумма двух максимальных чисел равна: {result}")
