# python_learn
print("Let's see how long you have lived in days,minutes and seconds.")
#定义变量名字，并弹出输出对话框
name = input("name:")
print("now enter your age")
#定义变量年龄，并弹出输出对话框
age= int(input("age:"))
#将输入的年龄转换成天数、分钟和秒
days=age*365
minutes=age*525948
seconeds=age*31556926
#输出最终结果给用户
print(name,"has been alive for",days,"days",minutes,"minutes and",seconeds,"seconds! wow!")