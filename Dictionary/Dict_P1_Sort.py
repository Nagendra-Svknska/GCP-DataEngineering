key_val={}
key_val['a']=4
key_val['b']=1
key_val['c']=5
key_val['d']=3
key_val['e']=2
print(key_val)


# for i in sorted(key_val.values()): #sort based on values
#         print(i)

# for i in sorted(key_val.keys()):    #sort based on keys
#         print(i)

# key_val.popitem()
print(key_val.values())
key_val.update({'f':34,'r':67})
print(key_val)

