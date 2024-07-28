# list = []
# list.append(1)
# list.append(2)
# list.append(3)
# list.append(4)
# list.append(5)
# list.append(6)
# list.append(7)
# list.append(8)
# list.append(9)
# list.append(10)
# print(list)

# list2 = [11,12]
# list.extend(list2)
# print(list)

# list3 = [1,3,4,5,6,7,8,9,10,11]
# for i in range(len(list3)):
#     print(list3[i])

list4 = [1,2,3,4,6,7,8,9,10,11]
list5 = []
for i in list4:
    if i %2 == 1:
        list5.append(i)
print(list4)
print(list5)