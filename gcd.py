#num1=int(input("enter number 1: "))
#num2=int(input("enter number 2: "))
num1=3
num2=5
def gcd(num1,num2):
    if num1>num2:
        small=num2
    else:
        small= num1
    for i in range(1,small+1):
        if num1%i==0 and num2%i==0:
            gcd=i
    lcm=(num1*num2)//gcd
    print("lcm of {} and {} is = {} \ngcd of {} and {} is = {}".format(num1,num2,lcm,num1,num2,gcd))
gcd(num1,num2)
