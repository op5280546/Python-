# 获取元组的一些基本信息

tuple1 = (9, 1, -4, 3, 7, 11, 3)

print('tuple1 =', len(tuple1))


print('tuple1.Max=', max(tuple1))


print('tuple1.Min=', min(tuple1))


print('tuple1.3={}'.format(tuple1.count(3)))


# 元组的改变？？？？

# tuple2 = ('a', 'c', 'd')
#
# tuple2[1] = 2


# 元组翻转 ??
# tuple3 = (1, 2, 3)
# tuple3.reverse()


# 元组排序 ??
#
# tuple4 = (9, 1, -4, 3, 7, 11, 3)
# tuple4.sort(reverse=True)

print(tuple1.index(9))
