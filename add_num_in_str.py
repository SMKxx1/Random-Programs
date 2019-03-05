a = input("Enter the string: ")
count = len(a)
Num = ""
Sum = 0
if a.isalpha():
    print(a,"has no numbers")
else:
    for i in range(0,count):
        if a[i].isdigit():
            Num = Num+a[i]   
        else:
            pass
    for i in range(0,len(Num)):
        Sum = Sum + int(Num[i])
    print(a,"has the digits",Num,"and the sum is",Sum)

        
