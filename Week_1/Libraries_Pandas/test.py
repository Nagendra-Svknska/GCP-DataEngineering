import  pandas as pd

cy=pd.DataFrame({'name':['rajes','mahesh','manish'],'age':[12,34,44],'city':['','','']},index=['ap','mh','mp'])
print(cy)
print("ans :",cy.iloc[2:])
# print(cy.loc['ap'])