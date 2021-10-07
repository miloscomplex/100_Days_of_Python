
numbers = [1,2,3]
new_numbers = [n + 1 for n in numbers]

print(new_numbers)


range_list = [num * 2 for num in range(1,5)]

short_names = [name for name in names if len(name) < 5]

# [new_item for item in items if test]

all_caps = [name.upper() for name in names if len(name) > 5]
