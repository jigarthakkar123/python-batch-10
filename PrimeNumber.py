num=int(input("Enter Number : "))

if num%2!=0:
    for i in range(3,int(num/2)+1,2):
        if num%i==0:
            print(num," Is Not Prime")
            break
    else:
        print(num," Is Prime")
else:
    print(num," Is Not Prime")
