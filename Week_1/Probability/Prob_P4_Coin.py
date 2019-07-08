import  itertools as it

def findTotalOutcomes(tries):
 h_val="h"*tries
 t_val="t"*tries
 # print("h_val :",h_val," t_val:",t_val)

 h_list=list(h_val)
 final_list=[h_val]

 for i in range(len(h_list)):
    temp_list =h_list.copy()
    for j in range(i):
     temp_list[j]="t"
     if("".join(temp_list)not in final_list):
        final_list.append("".join(temp_list))
    # print(final_list)
 final_list=findAllCombo(final_list, len(final_list))
 final_list.append(t_val)

 return final_list


def findAllCombo(temp_list,len_val):
    tem_val=[]
    final_list=[]

    for i in temp_list:
        # print("i value",i)
        tem_val = list(it.permutations(i, len_val))
        # print("tem values :",tem_val)

        for i in tem_val:
         if(i not in final_list):
            final_list.append(i)
    return final_list


no_coins=int(input("enter the no of coins"))
fin=findTotalOutcomes(no_coins)

abc=[]
for i in fin:
    abc.append("".join(i))
print("abc val:",abc,"length :",len(abc))
print("total no of outcomes :",len(abc))

count=0
int_probVal=int(input("enter the number of heads to check probability:"))

for i in abc:
    c=i.count('h')
    if(c==int_probVal):
        count+=1
print("no of possible ways :",count)
print("probability(no of possible ways/total no of outcomes) is :",count/len(abc))
