from operator import itemgetter

lis=[{"Name": "Rohan","age" : 21}, {"Name": "Mohit","age" : 23},
    {"Name": "Mahesh","age" : 18}]
print("Sorting by age")
print (sorted(lis,key=itemgetter('age')),"\n")

print("Sorted by Name & Age ")
print(sorted(lis,key=itemgetter('Name','age')))
print("Age in descending order")
print(sorted(lis,key=itemgetter('age'), reverse=True))


