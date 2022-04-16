#json.loads() to convert JSON string to a dictionary

import json

jsnString = """{
    "name": "keval",
    "salary": 15000,
    "skills": [
        "Python",
        "Odoo",
        "Web Development"
    ],
    "email": "keval123@sample.com",
    "projects": ["Odoo Training","Report Creating"]
}
"""

# print("Converting JSON string document to Python dictionary")
# pydict= json.loads(jsnString)
#
# print("Printing key and value")
# print(pydict["name"])
# print(pydict["salary"])
# print(pydict["skills"])
# print(pydict["email"])
# print(pydict["projects"])
#
# print("Converted")

#Parse and Retrieve nested JSON array key-values
print("Started reading nested json array")
pydict=json.loads(jsnString)
print("Project Name:", pydict["projects"])
print("Name of Programmer: ",pydict["name"])

