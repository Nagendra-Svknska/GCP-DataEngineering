import  numpy as np
import pandas as pd
lis_val=[12.23, 13.32, 100, 36.32]
print(np.array(lis_val,dtype=float))

p=np.matrix(range(2,10))

print("p value :",p)
p2=np.arange(2, 11).reshape(3,3)
print("p2 value :",p2)

d=np.array([1,2,3,4,5,6])
ser=pd.Series(d)
print("Ser value:",ser)
