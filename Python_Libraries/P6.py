import numpy as np

mat_val=np.ones((4,4))
print(mat)

# mat_val=mat.reshape(4,4)
# print(mat_val)

mat_val=np.pad(mat_val,pad_width=1,mode='constant',constant_values=0)
print(mat_val)

