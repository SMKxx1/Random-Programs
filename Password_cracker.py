import hashlib
import fileinput
import sys
import os

clear = lambda: os.system('cls')

def art():
    print('''

                                                                001                                         111
                01                             0         00      10                                         111                         1                        01
                 0           110               01                10                                                                     11                          10
       011       11                            10                 0                                                              01     11                       00
                 11                             1      11110      01                                                               10    0
             11   0      01111100               1      0   1      1  00111001                 000000111       1000                  0    1       0111                  0
  0            11  1            00010           1       01101     100      011    01       011       01     110  10                  0   0      0  1         1     0  00
 0             00   0001100101101100100          010100010001011010000001011010111011100010101101111000111011 01010          101011010   0100110001001111110111011001000
 0            01                                                                                                                               1  000
 101       1000                                                                                                                                11   0
   010001110                                                                                                                                      101
   
   ''')
art()


tac = ""

def replace(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

def encoder(password):
    password1 = hashlib.md5(password.encode())
    password = password1.hexdigest()
    return password


def secret_create(user, password):
    secret = input("Enter your secret: ")
    f = open("Password.txt", "r")
    lines = f.readlines()
    f.close()
    f = open("Password.txt", "w")
    for line in lines:
        if line != str({user: password}):
            f.write(line)
    f.write(str({user: password}) + " " + secret + "\n")
    print("Your secret has been saved!!!")
    f.close()


def secret_read(user, password):
    f = open("Password.txt", "r")
    lines = f.readlines()
    for line in lines:
        if str({user: password}) in line:
            tac = line
        else:
            print("Error: ")
    tac = tac.split()
    sec = tac[2:]
    sec = ' '.join(sec)
    print("Your secret is: ", sec)
    input()

def login2(user,password):
    password = encoder(password)
    print('''What do you want to do??
    1. Create a secret
    2. Read a secret
    3. Logout''')
    ch = input('> ')
    if ch == '1':
        secret_create(user, password)
        login2(user, password)
    elif ch == '2':
        secret_read(user, password)
        login2(user, password)
    else:
        pass

def login():
    count = 0
    while count < 3:
        user = input("Enter your username: ")
        password = input("Enter your password: ")
        password = encoder(password)
        user_pass_dictionary = str({user: password})
        if user_pass_dictionary in open("Password.txt").read():
            print()
            print("You are logged in now!!!")
            print('''What do you want to do??
1. Create a secret
2. Read a secret
3. Logout''')
            ch = input('> ')
            if ch == '1':
                secret_create(user,password)
                login2(user,password)
            elif ch == '2':
                secret_read(user,password)
                login2(user,password)
            elif ch == '3':
                main()
            else:
                print("I didn't quite get that")
                login2()
        else:
            print("Invalid Username or Password!!!")
            count += 1
            if count != 3:
                print("You have", 3 - count, "more attempts left")
                print()
            elif count == 3:
                print("Too many attempts...")
                break

def pass_creator():
    user = input("Enter your username: ")
    if user in open("Password.txt").read():
        print("Username already taken")
        input()
        main()
    password = input("Enter your password: ")
    password = encoder(password)
    f = open("Password.txt","a+")
    user_pass_dictionary = str({user:password}) + "\n"
    f.write(user_pass_dictionary)
    print("Your username and password has successfully been added")

def pass_changer():
    user = input("Enter your username: ")
    pass_old = input("Enter your old password: ")
    pass_old = encoder(pass_old)
    if str({user:pass_old}) in open("Password.txt").read():
        pass_new = input("Enter your new password: ")
        pass_new = encoder(pass_new)
        replace("Password.txt",str({user:pass_old}),str({user:pass_new}))
        print("Your password has been successfully changed")
    else:
        print("Invalid username or password")



def pass_reader():
    user_name = input("Enter the username: ")
    password = input("Enter the password: ")
    password1 = hashlib.md5(password.encode())
    password = password1.hexdigest()
    dictionary = str({user_name:password})
    if dictionary in open("Password.txt").read():
        print("Credentials Found!!!")
    else:
        print("Credentials Not Found!!!")

attempted_password = ""

def brute_login(user,password):
    count = 0
    while count < 3:
        user_pass_dictionary = str({user: password})
        if user_pass_dictionary in open("Password.txt").read():
            print()
            print("You are logged in now!!!")
            def secret_create():
                secret = input("Enter your secret: ")
                f = open("Password.txt", "r")
                lines = f.readlines()
                f.close()
                f = open("Password.txt", "w")
                for line in lines:
                    if line != str({user: password}) + "\n":
                        f.write(line)
                f.write(str({user: password}) + " " + secret + "\n")
                print("Your secret has been saved!!!")
                f.close()
            def secret_read():
                f = open("Password.txt","r")
                lines = f.readlines()
                for line in lines:
                    if str({user: password}) in line:
                        tac = line
                tac = tac.split()
                print("Your secret is",tac[2])
            break
    secret_read()

def brute():
    cc = 0
    list_of_chars = "\[\{\]\}'\:0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM "
    def solve_password(word):
        global attempted_password
        for character in word:
            for entry in list_of_chars:
                if character == entry:
                    attempted_password += character
                    print(attempted_password)
                    continue
        return attempted_password

    print("Enter the username to Bruteforce")
    user = input("> ")
    user = "{'"+user+"':"
    f = open("Password.txt","r")
    lines = f.readlines()
    f.close()
    f = open("Password.txt","r")
    for line in lines:
        if user in line:
            password2 = line
            password = solve_password(password2)
            if password in open("Password.txt").read():
                print()
                print("You have successfully Bruteforced into the account")
                brute_login(user,password)
            else:
                print("Bruteforce failed...")
            cc += 1
        else:
            pass
    if cc == 0:
        print(cc)
        print("No user found...")
    else:
        pass



def main():
    print("Please choose your option bellow")
    print("Enter 1 to create an username and password")
    print("Enter 2 to login using your username and password")
    print("Enter 3 to change your password")
    choice = input("> ")
    if choice == '1':
        pass_creator()
    elif choice == '2':
        login()
    elif choice == '3':
        pass_changer()
    elif choice == 'Brute' or 'brute':
        brute()
    else:
        pass

main()