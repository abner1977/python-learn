# i = 0
# total = 0
# while i <= 100:
#     total += i
#     i += 1
# print(f"sum = {total}")


# import random
#
# num = random.randint(1, 100)
# flag = True
# count = 0
# while flag:
#     guess = int(input("输入猜值"))
#     count += 1
#     if (guess == num):
#         print(f"猜中了{guess}")
#         flag = False
#     elif (guess > num):
#         print("猜大了")
#     else:
#         print("猜小了")
# print(f"猜了 {count} 次")
# 内置函数 end()  默认是 end('\n') 换行   不换行 置为空     \t 制表符 多个空格
# i = 0
# while i <= 10:
#     j = 0
#     while j <= 10:
#         print(f"内层{j}\t", end='|')
#         j += 1
#     i += 1
#     print(f"外层{i}")
# print("end")
