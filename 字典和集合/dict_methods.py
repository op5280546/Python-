d = {
    'Name': 'Jack',
    'Age': 9,
    'Grade': 5,
}

print(d.get("Name"))

print(d.keys())  # 所有 keys

print(d.values())  # 所有 values

print(d.items())  # All

c = d.pop('Name')  # 取出 pop

print(c)

print(d)

d.clear()  # 清空 clear

print(d)


# 字典的更新

c = {
    1: 1,
    2: 2
}

c[3] = 3
c[4] = 4

print(c)


d = {
    1: 5,
    6: 6
}

# c.update(d)
#
# print(c)

e = {**c, **d}  # 合併

print(e)
