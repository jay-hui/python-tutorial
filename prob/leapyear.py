n = int(input())
if (n%4==0):
    if(n%100==0):
        if(n%400==0):
            print("Yes.")
        else:   
            print("No and goodbye.")
    else:
        print("Yes.")
else:
     print("No and goodbye.")
        



####

n = int(input())
if (n % 400 == 0):
    print("Yes!")
else:
    if (n % 100 == 0):
        print("No!")
    else:
        if (n % 4 == 0):
            print("Yes!")
        else:
            print("No!")