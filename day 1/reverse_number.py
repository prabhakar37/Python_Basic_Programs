# reverse a number

num = int(input("enter number: "))
temp = num
reverse_num = 0

while num > 0:
    digit = num % 10
    reverse_num = reverse_num*10 + digit
    num = int(num/10)

print(f"reverse of {temp} is {reverse_num}")