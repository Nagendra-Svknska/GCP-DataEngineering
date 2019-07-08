from builtins import print


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

# print(full_name[::-1])

reverseVal(full_name)
# print("git test")



