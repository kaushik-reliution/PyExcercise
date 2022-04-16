#Find the length of the list and simply swap the first element with(n-1) element.

def swaplist(newlist):
    print("Calling function")
    size=len(newlist)
    # print(size)
    #swapping logic
    temp = newlist[0]
    newlist[0] = newlist[size-1]
    newlist[size-1] = temp
    return newlist

print("First come here")
swapped = [12,15,9,4,17]
print("Before",swapped,"\n")
print("After",swaplist(swapped))
