import calendar

stop = ""

while stop != 'stop':
    months = ["","january","february","march","april","may","june","july","august","september","october","november","december"]
    print("------Calendar Program in Python------\n")
    print("Enter 'x' for exit.")
    y = input("Enter Year: ")
    if y == 'x':
        break
    else:
        m = input("Enter month: ")
        if m.isalpha():
            m = months.index(m)
        else:
            pass
        yy = int(y)
        mm = int(m)
        print("\n",calendar.month(yy,mm))
    stop = input("If you want to stop type 'stop': ")
