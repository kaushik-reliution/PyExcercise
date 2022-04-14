# create one class named "product" with members "name", "code", "category", "Price
class product:
    print("Product Name")
    name=str(input())
    print("Code")
    code=int(input())
    print("Category")
    cat=str(input())
    print("Price")
    val=int(input())
def memb(self):
    print(self.name)
    print(self.code)
    print(self.cat)
    print(self.val)
prod=product()
print("Name is:-\n",prod.name,"Code is\n",prod.code,"Category is\n",prod.cat,"Price is:-",prod.val)

