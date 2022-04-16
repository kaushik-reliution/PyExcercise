import re
#re.search(pattern,string,flag=o)
# str_reg="Regular Expression Search Method"
# op=re.search(r"\breg",str_reg,re.I)
# print("match found",op)
# print("Matching Word",op.group())

#re.split()
split="Split method applied"
sp=re.split(r"\s+",split,maxsplit=1)#s+ gives in splited method and s- gives as one string
print("Split word",sp)
