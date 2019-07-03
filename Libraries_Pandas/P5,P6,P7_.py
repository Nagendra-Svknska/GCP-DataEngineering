import pandas as pd
dict_custom={"India":['Mumbai','Banglore','Chennai'],"France":['paris','',''],"USA":['New York','Chicago','NAN']}

# Prob 5 (create and display a DataFrame from a specified dictionary)
print(dict_custom)
dataFrame_samp=pd.DataFrame(dict_custom,index=[1,2,3])
print("Problem 5 :",dataFrame_samp)


# prob 6 (to display a summary of the basic information about a
# specified Data Frame and its data)
print("===================================")
print("Problem 6 :",dataFrame_samp.info())


# Prob 7 (program to get the first n rows of a given DataFrame)
print(dataFrame_samp.iloc[:2])


