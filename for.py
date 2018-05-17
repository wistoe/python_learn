print("let's guess the Number?")
num=133
result=False
while result==False:
    answer=int(input())
    if answer<num:
        print("too small!")
    if answer>num:
        print("too big!")
    if answer==num:
        print("Good!U are right!")
        result = True