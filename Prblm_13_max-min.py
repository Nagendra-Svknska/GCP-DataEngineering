from utils import prblm2 as util

valStr=input("enter values with a space:")
listVal=util.find_datatype(valStr.split())

# listVal.sort()
# print(listVal[0])                      #by using sort
# print(listVal[-1])

print("Maximum Value is :",util.findMaxOfList(listVal))
print("Minimum Value is :",util.findMinOfList(listVal))

