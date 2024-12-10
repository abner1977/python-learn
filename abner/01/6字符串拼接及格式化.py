print("11" + "22")
age = "33"
print("22" + age)
num = 11
#  直接拼接 数字 报错
print("55" + str(num))

# 占位符的方式  可以将数字和字符串拼接
message = "年龄是: %s" % age
print(message)
height = 180.23
message = "年龄是: %s, 分数是: %s ,身高: %.1f" % (age, num, height)
print(message)

#  %5d   5表示整体长度   .1f表示格式化小数
num1 = 11
num2 = 11.345
print("11=> %5d" % num1)
print("11.345=> %7.1f" % num2)
print("11.345=> %.1f" % num2)
