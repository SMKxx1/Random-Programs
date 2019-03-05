a = input("Enter your phone number: ")
if a[0] == "+" and a[3] == " " and a[7] == "-" and a[11] == "-":
    print("Valid Number")
else:
    print("Invalid Number")
        
