guess=0
x= int(input("enter an integer"))
if x < 0:
    neg_flag = True
while guess**2 < x:
    guess+=1
if guess**2 == x:
    print("square root of",x,"is",guess)
else:
    print(x,"is not a perfect square")
    if neg_flag:
        print("just checking did you mean",-x,"?")
