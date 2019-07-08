def listComprhension (temp_list):
    # sum_val = 0
    #sum_val = [sum := sum+i for i in temp_list] #from python 3.8 onwards
    sum_val = [i**2 for i in temp_list if i!=2]
    print("sumVal : ",sum_val)
    return sum_val



print(type(type(int)))
list1=[1,2,3,4]
print(listComprhension(list1))