# age = int(input("输入年龄"))
# if age > 18:
#     print(f"age = {age}, 已成年")
#
# print("祝您游玩愉快")

# money = int(input("请输入购票金额"))
#
# if money > 100:
#     print(f" 找余 {money - 100}")
# else:
#     print(f" 添补{100 - money}")
#
# print("给你商品")


# if int(input("年龄")) == 18:
#     print("刚刚成年")
# elif int(input("再次输入年龄")) > 18:
#     print("已成年")
# elif int(input("最后输入")) < 18:
#     print("未成年")
# else:
#     print("end")

age = int(input("输入年龄"))
if age > 18:
    if input("输入性别") == "男":
        print("男性成年")

    else:
        print("不符合招收要求")

else:
    print("未成年")
