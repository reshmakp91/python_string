str = input("Enter a string : ")
newstr = ""
for ch in str:
    if(ch not in newstr):
        newstr += ch
print("String after removing duplicates : ", newstr)