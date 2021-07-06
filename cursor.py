import functools
#################1###############
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print("ID of int_a:", id(int_a))
print("ID of str_b:", id(str_b))
print("ID of set_c:", id(set_c))
print("ID of lst_d:", id(lst_d))
print("ID of dict_e:", id(dict_e))
#################2###############
lst_d.append(4)
lst_d.append(5)
print('New ID of lst_d:', id(lst_d))
#################3###############
print("Type of int_a =", type(int_a))
print("Type of str_b =", type(str_b))
print("Type of set_c =", type(set_c))
print("Type of lst_d =", type(lst_d))
print("Type of dict_e =", type(dict_e))
#################4###############
print("Type of int_a =", isinstance(int_a, int))
print("Type of str_b =", isinstance(str_b, str))
print("Type of set_c =", isinstance(set_c, set))
print("Type of lst_d =", isinstance(lst_d, list))
print("Type of dict_e =", isinstance(dict_e, dict)
#################5###############
print("Anna has {} apples and {} peaches.".format(3,7))
#################6###############
print("Anna has {0} apples and {1} peaches.".format(3,7))
#################7###############
print("Anna has {apples} apples and {peaches} peaches.".format(apples=3,peaches=7))
#################8###############
print("Anna has {0:5} apples and {1:3} peaches.".format(3,7))
#################9###############
apples=3
peaches=7
print(f'Anna has {apples} apples and {peaches} peaches.')
#################10###############
print("Anna has %s apples and %s peaches" % (apples, peaches))
#################11###############
data_dict = {"app": apples, "peach": peaches}
print('Anna has %(app)s apples and %(peach)s peaches' % data_dict)
#################12###############
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)

list_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_comprehension)
#################13###############
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(list_comprehension)

lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)
#################14###############
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)

dc_with_if = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(dc_with_if)
#################15###############
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)

dc_with_elif = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(dc_with_elif)
#################16###############
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(dict_comprehension)

d = {}
for x in range(10):
    if x**3 % 4 == 0:
        d[x] = x**3
print(d)
#################17###############
dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension)

d = {}
for x in range(10):
    if x**3 % 4 == 0:
        d[x] = x**3
    else:
        d[x] = x
print(d)

#################18###############
def foo(x, y):
    if x < y:
        return x
    else:
        return y


foo = lambda x, y: x if x < y else y
print(foo(4, 9))

#################19###############
foo = lambda x, y, z: z if y < x and x > z else y


def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y


print(foo(8, 3, 12))
#################20###############
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))
#################21###############
print(sorted(lst_to_sort, reverse=True))
#################22###############
new_list = list(map(lambda x: x * 2, lst_to_sort))
print(new_list)
#################23###############
list_A = [2, 3, 4]
list_B = [5, 6, 7]

list_comp = [list_A[idx] ** list_B[idx] for idx, item in enumerate(list_A)]
print(list_comp)
#################24###############
red_l = functools.reduce(lambda x, y: x + y, lst_to_sort)
print(red_l)
#################25###############
new_list = list(filter(lambda x: (x % 2 == 1), lst_to_sort))
print(new_list)
#################26###############
b = range(-10, 10)
negative = list(filter(lambda x: x < 0, b))
print(negative)
#################27###############
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
common = list(filter(lambda x: x in list_1, list_2))
print(common)
