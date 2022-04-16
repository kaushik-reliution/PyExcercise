# import re
# str=" Regular expression has 14 and 54 and 65 and 85 and 95"
# # chk=re.findall(r"\d",str)#it gives all the string related to numbers
# iter=re.finditer(r"\d{2}",str)#it gives all the possible matches
# for match in iter:
#     print(match)
#     print(match.group())

import re
str=" Python program gives you reliability,reusability and Reproductivity. also give better programming experience"
print(re.findall(r"\b[r]\w+\b",str,re.I))
print(re.findall(r"\b[p]\w+\b",str,re.I))#re.i ignore uppercase or lowecase..
print(re.findall(r"\b[pr]\w+[n]",str,re.I))

