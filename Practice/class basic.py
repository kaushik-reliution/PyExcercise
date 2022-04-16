class Human:
    def __init__(self,n,w,r):
        self.name=n
        self.work=w
        self.raag=r
 
    def dwork(self):
        if self.work=="musician":
            print(self.name,"Compose music")
        elif self.work=="singer":
            print(self.name,"sing a song")
    def draag(self):
        if self.raag=="Shudh Yaman":
            print(self.name,"Kyan Guman Karna")
        elif self.work=="Mishra Yaman":
            print(self.name,"Wo Jab Yaad Aaye")

Vicks=Human("Vivek Shukla","singer","Shudh Yaman")
Vicks.dwork()
Vicks.draag()

