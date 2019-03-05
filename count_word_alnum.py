a = input("Enter a sentence: ")
count = 0
for i in range(0,len(a)):
    if a[i] == " ":
        count+=1
    else:
        pass
print("There are",count+1,"words in the sentence, ",end="")
print(len(a),"is the number of charecters in the sentence and ",end="")
count = 0
for i in a:
    if i.isalnum():
        count+=1
    else:
        pass
per = (count/len(a))*100
per = int(per)
print(per,"percentage of the charecters are Alpha Numeric")
