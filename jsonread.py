# import json
#
# print("Start Reading a File")
# with open("skip.json","r") as rd:
#     read_file=json.load(rd)
#
#     print("Retrieving data from a file ")
#     for key,value in read_file.items():#read data line by line
#         print(key,":",value)
#     print("Retrieved")

import json

with open("skip.json","r") as rd:
    rdfil=json.load(rd)
    print("Without using for loop")

    print("Name:- ", rdfil["Name"])
    print("Places:-\b", rdfil["Places"])
    print("State:- \b", rdfil["State:"])#\b-backspace

    print("Access data directly using key name")