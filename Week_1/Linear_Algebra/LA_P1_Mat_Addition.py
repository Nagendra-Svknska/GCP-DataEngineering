list_val1=[[1,2,3],[5,6,7]]
list_val2=[[11,21,31],[51,61,71]]
res=[[0,0,0],[0,0,0]]
# res=[]
print("matrix 1:",list_val1)
print("matrix 2:",list_val2)

# result=[[list_val1[a][b] +list_val2[a][b]for a in range(len(list_val1))] for b in range(len(list_val2[0]))]
# result = [[list_val1[i][j] + list_val2[i][j]  for j in range(len(list_val1[0]))] for i in range(len(list_val1))]
# print("result :",result)
for i in range(len(list_val1)):
    # print(list_val1[i])
    for j in range(len(list_val1[i])):
        # print(list_val1[i][j])
        res[i][j]=list_val1[i][j]+list_val2[i][j]
print("Result matrix",res)