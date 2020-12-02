#def division ():
#     arg_1 = float(input("Введите первое число:" ))
#     arg_2 = float(input("Введите второе число:" ))
#     result = arg_1 / arg_2
#     return result
#
# result_division = division()
# print(result_division)

def division (arg_1, arg_2):
     if arg_2 == 0:
         result = (f"Делить на {arg_2} нельзя.")
         return result
     else:
        result = round(arg_1 / arg_2, 2)
        return result
arg_1 = float(input("Введите первое число:" ))
arg_2 = float(input("Введите второе число:" ))
result_division = division(arg_1, arg_2)
print(result_division)
