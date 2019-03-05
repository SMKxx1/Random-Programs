from math import pi

def rec(l,b):
    area = l*b
    peri = 2*(l+b)
    print("The area of the Rectangle is",area,"and the perimeter is",peri)

def tri(b,h):
    area = 1/2*(b*h)
    print("The area of the triangle is",area)

def cone(r,l,h):
    area = pi*r*l
    vol = (1/3)*pi*(r**2)*h
    print("The area of the cone is",area,"and the volume is",vol)

def cyl(r,h):
    area = (2*pi*r*h) + (2*pi*(r**2))
    vol = pi*(r**2)*h
    print("The area of the cylinder is",area,"and the volume is",vol)

def sph(r):
    area = 4*pi*(r**2)
    vol = (4/3)*pi*(r**3)
    print("The area of the sphere is",area,"and the volume is",vol)
def pro():
    print("Please select your choice below")
    print("Enter 1 to calculate a Rectangle's details")
    print("Enter 2 to calculate a Triangle's details")
    print("Enter 3 to calculate a Cone's details")
    print("Enter 4 to calculate a Cylinder's details")
    print("Enter 5 to calculate a Sphere's details")
    print("Enter 6 to calculate ALL")
    choice = input(">>> ")
    def pro2():
        print()
        print("Please enter the values of the Length and the Breath of the rectangle")
        l_rec = int(input("Length: "))
        b_rec = int(input("Breath: "))
        print()
        print("Please enter the values of the Base and the Height of the triangle")
        b_tri = int(input("Base: "))
        h_tri = int(input("Height: "))
        print()
        print("Please enter the values of the Radius, Length and Height of the cone")
        r_cone = int(input("Radius: "))
        l_cone = int(input("Length: "))
        h_cone = int(input("Height: "))
        print()
        print("Please enter the values of the Radius and the Height of the cylinder")
        r_cyl = int(input("Radius: "))
        h_cyl = int(input("Height: "))
        print()
        print("Please enter the Radius of the sphere")
        r_sph = int(input("Radius: "))
        print()
        rec(l_rec,b_rec)
        tri(b_tri,h_tri)
        cone(r_cone,l_cone,h_cone)
        cyl(r_cyl,h_cyl)
        sph(r_sph)
    def loop():
        print("Invalid choice")
        print("Wanna try again??")
        c = input("(y/n) ")
        if c == 'y':
            pro()
        elif c == 'n':
            pass
        else:
            print("I don't know what that means...")
            print("I assume you want to end the program...")
    if choice == '1':
        print()
        print("Please enter the values of the Length and the Breath of the rectangle")
        l_rec = int(input("Length: "))
        b_rec = int(input("Breath: "))
        print()
        rec(l_rec, b_rec)
    elif choice == '2':
        print()
        print("Please enter the values of the Base and the Height of the triangle")
        b_tri = int(input("Base: "))
        h_tri = int(input("Height: "))
        print()
        tri(b_tri, h_tri)
    elif choice == '3':
        print()
        print("Please enter the values of the Radius, Length and Height of the cone")
        r_cone = int(input("Radius: "))
        l_cone = int(input("Length: "))
        h_cone = int(input("Height: "))
        print()
        cone(r_cone, l_cone, h_cone)
    elif choice == '4':
        print()
        print("Please enter the values of the Radius and the Height of the cylinder")
        r_cyl = int(input("Radius: "))
        h_cyl = int(input("Height: "))
        print()
        cyl(r_cyl, h_cyl)
    elif choice == '5':
        print()
        print("Please enter the Radius of the sphere")
        r_sph = int(input("Radius: "))
        print()
        sph(r_sph)
    elif choice == '6':
        pro2()
    else:
        loop()
pro()