def items():
    dic = {}
    print("Enter the items")
    items = input("> ")
    items = items.split()
    total_price = 0
    for i in items:
        print("Enter the price of",i)
        price = int(input("> "))
        total_price += price
        dic[i] = price
    items = []
    for i in dic:
        f = "| " + "{0:12}                                       Rs. {1:8}".format(i,dic[i]) + " |"
        items.append(f)
    gst = (total_price/100) * 9
    gst = round(gst)
    total_price += gst*2
    return items, gst, total_price

def item_format(items,gst,total_price):
    for i in items:
        print(i)
    print("|", " " * 63, "|")
    print("|", "SGST (9%)                                          Rs. {0:8}".format(gst), "|")
    print("|", "CGST (9%)                                          Rs. {0:8}".format(gst), "|")
    print("|"," "*49,"______________|")
    print("|","Total Price:                                       RS. {0:8}".format(total_price),"|")




def format():
    print("Would You Like To\n1. Dine in\n2. Take away")
    opt = input("> ")
    print()
    if opt == '1':
        o = "  Dine in"
    elif opt == '2':
        o = 'Take away'
    else:
        print("Invalid Option")
        print("Trying again...")
        input()
    i, g, t = items()
    print()
    print("|","-"*63,"|")
    print("|","Ayush Hotel"," "*41,o,"|")
    print("|","-"*63,"|")
    print("|","ITEMS \t\t\t\t\t\t\t\t\t\t\t\t\tPRICE","|")
    print("|"," "*63,"|")
    item_format(i, g, t)
    print("|","-"*63,"|")
format()