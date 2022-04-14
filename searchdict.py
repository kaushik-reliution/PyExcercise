import collections

# prod_srch={"Drink" : "15","Food" : "89","Groccery" : "007"}
# print(prod_srch.get("Drink", "Not Found"))
# print(prod_srch.get("Junk food","Not Found"))

#using defaultdict long program

# def_srch=collections.defaultdict()
#
# key=input("Enter key")
# def_srch["a"] = 4
# def_srch["b"] = 10
#
# if key == "a":
#     print("Value of A is :-", def_srch["a"])
# elif key =="b":
#     print("value of B is ", def_srch["b"])
# else:
#     print("Value of c is not found")

#using defaultdict sort program using lambda

def_srch=collections.defaultdict(lambda: 'not found')#When def_srch not able to get value of c it is forward to lambda
key=input("Enter key")
def_srch["a"] = 4
def_srch["b"] = 10
print("Value of A is :-", def_srch["a"])
print("value of B is ", def_srch["b"])
print("value of C is ", def_srch["c"])


