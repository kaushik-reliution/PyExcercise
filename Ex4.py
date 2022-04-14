import random
# class category:
#     no_of_prod = 0
#     def __init__(self):
#         self.cname = str(input("enter catogary name"))
#         self.c_code = int(input("enter category code"))
#         category.no_of_prod +=1
#     def dispcat(self):
#         print("Name",self.cname,"Category code",self.c_code)

class product(object):

    def __init__(self):
        print("Class Running")
        self.pname=""
        self.pcat=""
        self.pcode=0
        self.price=0

    def insertd(self):
        self.pname=str(input("Enter Product Name"))
        self.pcat=str(input("Enter Product Category"))
        self.price=int(input("Enter Price of product"))


    def dispval(self):
        print("Product name is",self.pname)
        print("Product cat is", self.pcat)
        print("Price of product",self.price)
        self.pcode=random.randint(0,100)


plist=[]
for i in range(2):
    pboj=product()
    pboj.insertd()
    plist.append(pboj)
for i in range(2):
    print("-----------------------")
    plist[i].dispval()
    print("-----------------------")



# obj1=category()
# obj2=category()
# obj3=category()
# obj1.dispcat()
# obj2.dispcat()
# obj3.dispcat()
# print("TOtal number of products",category.no_of_prod)