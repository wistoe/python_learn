num2=12
print("guess what i think?")
bingo=False
while bingo==False:
   answer=int(input())
   if  answer<num2 :
    print("too small!")
   if  answer>num2:
    print("too big!")
   if answer==num2:
    print("U are rghit!")
    bingo=True
