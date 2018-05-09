num=1233
print("guess what i think?")
answer=int(input())

result=(answer<num)
print("too small")
print(result)

result=answer>num
print("too big")
print(result)

result=answer==num
print("equal?")
print(result)