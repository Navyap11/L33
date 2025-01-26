num= int(input("Enter a number: "))
sum=0
temp=num
while temp>0:
    number= temp%10
    sum= sum+ number**3
    temp//=10

if num==sum:
    print("number:",num,"is an armstrong number")

else:
    print("is not an armstrong number")