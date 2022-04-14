
def swaplist(newlist):
    print("calling")

    newlist[3], newlist[0] = newlist[0], newlist[3]
    return newlist

slist = [12,34,54,67,89]
print(swaplist(slist))
