def swaplist(list):
    first = list.pop(5)
    last= list.pop(1)

    list.insert(0,last)
    list.append(first)
    return list
lis=[12,35,67,89,98,554]
print(swaplist(lis))