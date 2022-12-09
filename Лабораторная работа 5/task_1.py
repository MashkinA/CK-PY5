from pprint import pprint
dict_ = []
for i in range(16):
    a = {'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)}
    dict_.append(a)
pprint(dict_)
