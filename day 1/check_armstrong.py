# Armstrong number 153,370,371

num = int(input("enter any positive number: "))
temp = num
armst =0
power = 0

while(num > 0):
    num = int(num/10)
    power +=1

num = temp    # original num for armstrong
while num > 0:
    digit = num % 10
    armst += (digit ** power)
    num = int(num/10)        # num //= 10  


if temp == armst:
    print(f"{temp} is armstrong number")
else:
    print(f"{temp} is not a armstrong number")