sqrlist=[2,4,6,3,8]
sqr=[]
for i in sqrlist:
        sqr.append(i * i)
        print("Loop iteration",sqr)
        sqr.sort()
print("Final Output with sorting:-",sqr)