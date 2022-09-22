# 获取列表的一些基本信息

list1 = [9, 1, -4, 3, 7, 11, 3]

#print('list1 =', len(list1))
#print('list1.Max=', max(list1))
#print('list1.Min=', min(list1))
# print('list1.3={}'.format(list1.count(3)))

# append 結尾插入
# insert 中間插入
# remove 刪除
# reverse 翻轉
# sort 排序 (不改為正序,reverse為倒序)


# 列表的改变

list2 = ['a', 'c', 'd']

# 给list2结尾添加一个新元素 'e'
list2.append('e')
#print('list2=', list2)


# 在list2的'a'和'c'之间插入一个 'b'
list2.insert(1, 'b')
#print('list2=', list2)

# 删除list2里的'b'
list2.remove('b')
#print('list2=', list2)


# 更改元素
list2[0] = '1'
#print('list2=', list2)


#a = '123'
#a[0] = 'a'
#a = 'abc'


# 列表翻转
list3 = [1, 2, 3]
list3.reverse()
#print('list3=', list3)


# 列表排序

list4 = [9, 1, -4, 3, 7, 11, 3]
list4.sort(reverse=True)
#print('list4=', list4)


list5 = [1, 'a', 3, [1, 2], 'c']

# print(max(list5))
print(format(list5.count(1)))
list5.append('b')
list5.insert(1, 2)
list5.remove('b')
list5[2] = 3
list5[3] = 4

list5.reverse()  # 先排字符串>列表>整數
# list5.sort(reverse=True) 無法倒序
print(list5)
