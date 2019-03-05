n = int(input("Enter the range: "))
if n%2==0:
    n=n-1
    while n>=0:
        print(n)
        n=n-2
else:
    while n>=0:
        print(n)
        n-=2
