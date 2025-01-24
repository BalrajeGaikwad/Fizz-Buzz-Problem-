def fizz_buzz(number):
    if number%3==0 and number%5==0:
        return "Fizz Buzzzz"
    elif number%3==0:
        return "Fizzzz"
    elif number%5==0:
        return "Buzzz"
    else:
        return str(number)


user=input("Enter the number :-")
number_list=list(map(int,user.split()))

#l1=[12,45,3,45,5,6,43]
#l=int(input("Enter the number"))
output=[]
for num in number_list:
    result=fizz_buzz(num)
    output.append(result)
print(output)