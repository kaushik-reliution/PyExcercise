# import json
# fil={'name': 'File creating using json','address':'within this path',"Success":"Yes"}
# f=json.dumps(fil)
# with open("write.txt","w") as F:
#     F.write(f)

#Another way: write file using json using dump
# import json
#
# f1 = {"Name": "Advance python",
#       "Email:": "Pycode@sample.com",
#       "Address": "virtual",
#       }
# print("Started writing JSON data into a file")
# with open("jsn.json", "w") as write:
#     json.dump(f1, write, indent=1, separators=(",",": "), sort_keys=True) # Insert dict values in much pretty manner.
# print("Done writing JSON data")

#write a file using skipkeys to skip specific object

import json
class info:
    def __init__(self, name, age):
        self.name= name
        self.age= age
    def show_info(self):
        print("Name:", +self.name, "Age is", +self.age)

prog = info("Harappa", 5000)

prog_dict= {
        info: prog,#skipped object
        "Name" : "Indus valley Civilisation",
        "Places": ["Lothal","Dholavira","Rojadi"],
        "State:": "Gujarat",
}
print("Writing file by skiping keys ")
with open("skip.json","w") as wr:
    json.dump(prog_dict,wr,skipkeys=True)#info object skipped using skipkeys
print("done")




