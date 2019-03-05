line = input("Enter a line: ")
ucase = lcase = 0
alpha = digi = special = 0
for i in line:
    if i.isalpha():
        alpha+=1
    else:
        pass
    if i.isupper():
        ucase+=1
    elif i.islower():
        lcase+=1
    elif i.isdigit():
        digi+=1
    else:
        special+=1
print('''
Number of upper case:''',ucase,'''
Number of lower case:''',lcase,'''
Number of Alphabets:''',alpha,'''
Number of Digits:''',digi,'''
Number of special characters:''',special)