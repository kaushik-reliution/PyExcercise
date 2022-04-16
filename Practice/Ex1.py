class category:
    print("Enter Name:-")
    name = str(input())
    print("Enter Code:-")
    code = int(input())
    print("Enter Prod Numb:-")
    prod = int(input())

    def members(self):
        print("Name is ", self.name)
        print("COde is ", self.code)
        print("Product Number is", self.prod)

cat = category()
print("Name is",cat.name, "\nCode is ", cat.code, "\nProd no is", cat.prod)

