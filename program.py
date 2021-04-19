print("ENTER 1 TO ADD A CONTACT")
print("ENTER 2 TO FIND A CONTACT")
print("ENTER 3 TO DISPLAY ALL THE SAVED CONTACTS")
phonebook={ }
while True:
    num=int(input("ENTER 1/2/3 : "))
    if num==1:
        name=input("ENTER NAME OF NEW CONTACT : ")
        phno=int(input("ENTER PHNO : "))
        phonebook[name]=phno
    elif num==2:
        index=0
        search=input("ENTER CONTACT NAME YOU ARE LOOKING FOR : ")
        for element in phonebook.keys():
            index+=1
            if element==search:
                print(element," -- ",phonebook[element])
                break
            elif (index==len(phonebook)):
                print("NO CONTACT FOUND.....")
    elif num==3:
        print("--------------------------")
        print("CONTACT LIST")
        print("--------------------------")
        for element in phonebook.keys():
            print(element)
            print(phonebook[element])
            print()
        print("--------------------------")
