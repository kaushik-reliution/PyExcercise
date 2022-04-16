class category:
    #enter attribute's values through input
    print("Product Name")
    name = str(input())
    print("Code")
    code = int(input())
    print("Product")
    no_of_produ = int(input())

    def attr(self):
        print("Product name :-",self.name)
        print("Product code :-",self.code)
        print("No of Product :-", self.no_of_produ)

obj=category()
print("Object called")
obj.attr()



