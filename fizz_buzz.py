"""
# 1. Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz"

If the number is a multiple of 3 the output should be "Fizz" .
If the number given is a multiple of 5, the output should be "Buzz";.
If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz";.
If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the
examples below.
The output should always be a string even if it is not a multiple of 3 or 5.
Ex. L1=[12,5,7,20,19,30,35]
"""

def fizz_buzz(number):
    if number%3==0 and number%5==0:
        return "Fizz Buzzzz"
    elif number%3==0:
        return "Fizzzz"
    elif number%5==0:
        return "Buzzz"
    else:
        return str(number)

l1=[12,45,3,45,5,6,43]
l=int(input("Enter the number"))
output=[]
for num in l1:
    result=fizz_buzz(num)
    output.append(result)
print(output)