p=int(input("ENTER YOUR PROJECT SCORE"))
i=int(input("ENTER YOUR INTERNAL SCORE"))
e=int(input("ENTER YOUR EXTERNAL SCORE"))

if p>50 and i>50 and e>50:
    total = (0.7 * p) + (0.1 * i) + (0.2 * e)
    print(f'total is {total}')
    if total > 90:
        print("A+")

    elif total > 80:
        print("B+")

    else:
        print("c+")
else:
    if(p<50):
        print("failed in project")
    if(i<50):
        print("failed in internal")
    if(e<50):
        print("failed in external")