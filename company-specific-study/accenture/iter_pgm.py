nums=list(range(1,11))

i_nums=iter(nums)

print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))

try:
    print(next(i_nums))
    print(next(i_nums))
except Exception as e:
    print('no more loops')
else:
    print('okay')
finally:
    print('finally')
