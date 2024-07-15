# resoult = 0 
# for i in range(10):
#     resoult += i
# print(resoult)


# for i in range(15):
#     print(i**2)



# result = 0
# for i in range(5):
#     result += i**2#result += i igivea rac result = result + i
# print(result)


# for i in range(100):
#     if i %3 == 0 and i %5 == 0:
#         print(i)


# for i in range(10,0,-1):
#     print(i)


# result = 0
# age = int(input("enter your age:"))
# while age > 0:
#     age -= 1
#     result += age  
# print(result)


# num = 10
# while num > 0:
#     num -= 1
#     print(num) 


# num = 101
# result = 0
# while num > 0:
#     num -= 1
#     result += num
# print(result)    


# num = 11
# result = 0
# while num > 0:
#     num -= 1
#     result += num **2
# print(result)


# year = int(input("enter a year:"))
# if year %4 == 0:
#     print("makiani weli")
# else:
#     print("not nakiani")


num = (input("enter word:"))
if num == num[::-1]:
    print("number is palindrome")
else:
    print("not palindrome")