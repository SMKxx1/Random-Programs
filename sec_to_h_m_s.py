time = int(input("Enter the number of seconds: "))
s = time%60
m = time//60
h = time//3600
if h>=1:
    m%=60
else:
    pass
print(h,":",m,":",s,sep="")
