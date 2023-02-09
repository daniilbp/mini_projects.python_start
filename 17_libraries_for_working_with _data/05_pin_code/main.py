import itertools


num_list = [num for num in range(10)]

for item in itertools.product(num_list, num_list, num_list, num_list):
    print(*item)

# for item in itertools.product(num_list, repeat=4):
# for item in itertools.product(range(10), repeat=4):
#     print(*item)

# for i in range(10000):
#     print(str(i).rjust(4, '0'))
#     print('%04d' % i)
#     print(str(i).zfill(4))
#     print('{:04n}'.format(i))
#     print(f'{i:04n}')
