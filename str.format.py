from unicodedata import name

name = 'python'
age = 27

new_str = 'I am ' + name + ',' + str(age) + ' years old'

print(new_str)

new_str_1 = 'I am %s,%d years old' % (name, age)

print(new_str_1)

new_str_2 = 'I am {},{} years old'.format(name, age)

print(new_str_2)

# 推薦
new_str_3 = 'I am {name},{age} years old'.format(
    name='asd', age='dsa'
)

print(new_str_3)

# 推薦
name1 = 'fgh'
age1 = 30
new_str_4 = f'I am {name1},{age1} years old'

print(new_str_4)
