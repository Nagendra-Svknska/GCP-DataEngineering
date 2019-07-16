import pickle
import  numpy as np

pi=open('test_pickle.sav','rb')
resu=pickle.load(pi)
print(resu.predict([[67]]))

pi2=open('test_pickle2.sav','rb')
resu2=pickle.load(pi2)

# scc = resu2.fit_transform(26)
sc_Val =  resu2[67]
# sc=open('test_pickle.sav','rb')
# sc_Result = pickle.load(sc)
print(resu.predict([sc_Val]))


