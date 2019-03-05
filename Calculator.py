def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def multi(x,y):
    return x * y

def div(x,y):
    return x / y

def mod(x,y):
    return x % y

def floor(x,y):
    return x // y

def expo(x,y):
    return x ** y

def calculator():
    ans = input("Enter your first number: ")
    while True:
        print('''
Choose your option or Enter a equation
1. Add
2. Subtract
3. Divide
4. Multiply
5. Mod
6. Floor Division
7. To The Power Of

Type stop or s to stop
''')
        print(ans)
        opt = input("> ")
        if opt == '1':
            eq = input("Enter the number: ")
            ans = add(eval(ans),eval(eq))
            ans = str(ans)
            print(ans)
            input()
        elif opt == '2':
            eq = input("Enter the number: ")
            ans = sub(eval(ans),eval(eq))
            ans = str(ans)
            print(ans)
            input()
        elif opt == '3':
            eq = input("Enter the number: ")
            ans = div(eval(ans),eval(eq))
            ans = str(ans)
            print(ans)
            input()
        elif opt == '4':
            eq = input("Enter the number: ")
            ans = multi(eval(ans),eval(eq))
            ans = str(ans)
            print(ans)
            input()
        elif opt == '5':
            eq = input("Enter the number: ")
            ans = mod(eval(ans),eval(eq))
            ans = str(ans)
            print(ans)
            input()
        elif opt == '6':
            eq = input("Enter the number: ")
            ans = floor(eval(ans),eval(eq))
            ans = str(ans)
            print(ans)
            input()
        elif opt == '7':
            eq = input("Enter the number: ")
            ans = expo(eval(ans),eval(eq))
            input()
        elif opt == 'stop' or opt == 's':
            break
        else:
            eq = ans + opt
            ans = eval(eq)
            ans = str(ans)
            print(ans)
            input()


calculator()
