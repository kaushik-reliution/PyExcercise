#problem:Store monthly expenses in a list and find out total expenses for all months
# exp = [4300,2100,2450,5310,6800]
# total=0
# for item in exp:
#     total =total + item
# print(total)
# Prob; Search a home key in locations
# key_locate="chair"
# locations=["Bathroom", "living room","balcony","chair","basement"]
# for item in locations:
#     if item == key_locate:
#         print("Key is found in ",item)
#         break
#     else:
#         print("key is not found in",item)
# Prob: Print square of numbers to 5 except even numbers
for i in range(1,6):
    if i%2 == 0:
        continue #skip code which is below the continue line
    print(i*i)
