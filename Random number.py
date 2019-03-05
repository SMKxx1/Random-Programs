import random
def main():
    min = int(input("Enter the minimum number: "))
    max = int(input("Enter the maximum number: "))
    roll = "yes"
    while roll == "yes" or roll == "y" or roll == " ":
        print("The random number is:", random.randint(min, max))
        
        roll = input("Wanna roll again??: ")
        
if __name__=='__main__':
    main()
