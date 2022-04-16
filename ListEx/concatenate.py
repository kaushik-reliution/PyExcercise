# list1 = ["Th","i","th","exam","o","concat"]
# list2 = ["is","s","e","ple","f","enate"]
# print("Before Concatenate\n", list1, "\n", list2)
# list3 = [i + j for i, j in zip(list1, list2)]
# print(list3)

list1 = ["Shri","jai"]
list2 = ["ram","Ram"]
print("Before Concatenate\n", list1, "\n", list2)
list3 = [i + j for i in list1 for j in list2]
print(list3)