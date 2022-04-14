class Food:
    def general_usage(self):
        print("General Use: for Eating")
class Organic(Food):
        def __init__(self):
            print("organic food area")
            self.name1=["Cow Milk","Peanuts"]
            print(self.name1)
        def specific_use(self):
            print("Gives Energy and long life",self.name1)
class Inorganic(Food,):
        def __init__(self):
            print("Inorganic food area")
            self.namei=["Berger","Pizza"]
            print(self.namei)
        def specific_use(self):
            print("Gives lest energy and reduce life by gradually",self.namei)
o=Organic()
o.general_usage()

