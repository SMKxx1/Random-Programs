#Program to find the largest number in the list
a =[]
n = int(input("Enter the number of eliments: "))
for i in range(1,n+1):
    b = int(input("Enter the number: "))
    a.append(b)
a.sort()
print("The largest number is: ",a[n-1])
