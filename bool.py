num2=1233
print("guess what i think?")
answer=int(input())


result=(answer < num2)
print("too small")
print(result)

result= answer > num2
print("too big")
print(result)

result= answer == num2
print("equal?")
print(result)