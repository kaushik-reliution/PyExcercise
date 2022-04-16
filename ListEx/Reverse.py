list1=[20,10,50,60,80]
print("Original list",list1)
list2=[]
for item in list1:
    list2.insert(0, item)#When we insert an element at the first index in the list, the rest of the elements get shifted to the next index.
print("Reversed List",list2)#[80][60,80]...so on....





