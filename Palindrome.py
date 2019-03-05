s = str(input("Enter an word: "))
a = s[::-1]
if (a==s):
    print ("{0} It is a Palindrome".format(s))
else:
    print ("{0} It is not a Palindrome".format(s))
