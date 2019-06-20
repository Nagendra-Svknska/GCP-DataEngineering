def reverseVal(name):
    pat=" "

    for i in name:
        pat=i+pat
        print(pat)

firstName=input("Enter The First Name :")
print(firstName)
lastName=input("Enter The Last Name :")
print(lastName)
full_name=firstName+" "+lastName;

reverseVal(full_name)
print("git test")



