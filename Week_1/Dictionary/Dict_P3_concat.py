dict_custom={0: 10,1:20,2:22,3:77}
print(dict_custom)
dict_custom2={4: 100,22:220,12:202,3:770}
d_dummy=dict_custom.update(dict_custom2)   #existing dict_custom will be updated not a updated value will be retuned
#print(d_dummy)                            #this will be none not the updated dictionar assigned
print(dict_custom)
