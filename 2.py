n=int(input("ENTER YOUR SALARY"))
if n<10000 :
    hra=0.67*n
    da=0.73*n

elif n<20000 :
    hra=0.69*n
    da = 0.76*n

else:
    hra = 0.73*n
    da = 0.89*n

gs = hra + da + n
print(f"gross salary is {gs}")