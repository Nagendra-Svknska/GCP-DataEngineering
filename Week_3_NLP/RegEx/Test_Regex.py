import re

sse='''
Janis is 22 and Theon is 23  
Rajesh is 3 and Swarna is 41'''
# abc=open('')
ages=re.findall(r'\d{1,2}',sse)
print(ages)


import nltk
exp=r"""chunk: {}"""
nltk.RegexpParser()