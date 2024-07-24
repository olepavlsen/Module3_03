def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = ['string', True, 7]
print_params(values_list)
print_params(*values_list)
values_dict = {'a': False, 'b': 'letter', 'c': 9}
print_params(values_dict)
print_params(**values_dict)
values_list_2 = ['word', 34.788]
print_params(*values_list_2, 42)

