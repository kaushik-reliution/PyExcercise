list1 = [10,20,40,[50,[90,70,58],78],60,80]
list2 = [120,150]
print("Before add\t",list1)
list1[3][1].extend(list2)
print("Extend list:\n", list1)
for i in list1[3][1]:
    print("----******------")
    print("List of [3][1] :- ", i)
