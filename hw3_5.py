
# def sum_sum():
#     line = input("введите строку: ")
#     number_str = []
#     number_str = line.split()
#     number_int = list(map(int,number_str))
#     number_summ = sum(number_int)
#     return number_summ
#
#
# summ = sum_sum()
# print(f"Сумма введеных значений равна: {summ}.")

def sum_sum():
    stop = ("w")
    number_summ_all = 0
    while stop != ("q"):
        number_summ = []
        line = input("введите строку: ")
        number_str = []
        number_str = line.split()
        st = 0
        st = number_str.count("q")
        if st >0:
            # number_str.index("q")
            number_int = list(map(int, number_str[0: number_str.index("q")]))
            # number_str.remove("q")
            # number_int = list(map(int, number_str))
            number_summ = sum(number_int)
            number_summ_all += number_summ
            return number_summ_all
        number_int = list(map(int,number_str))
        number_summ = sum(number_int)
        number_summ_all += number_summ
        stop = input(f"Сумма всех значений равна: {number_summ_all}. Если желаете продолжить введите w, для завршения введите q:")
    return number_summ_all


summ = sum_sum()
print(f"Сумма введеных значений равна: {summ}.")