X_val = [[12,7,3],
[4 ,5,6],
[7 ,8,9]]
res=[[X_val[i][j]*9 for j in range(len(X_val[0]))] for i in range(len(X_val))]
print(res)


# for i in range(len(X_val)):
#     print(i)
#     for j in range(len(X_val[0])):
#         print("i:",i," j:",j)
