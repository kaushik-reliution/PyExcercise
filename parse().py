import json
def roundfloats(salary):
    return round(float(salary),2)
def deduct(leave):
    daywise=325
    return int(leave) * daywise
with open("jsn.json","r") as prse:
    readf=json.load(prse, parse_float=roundfloats, parse_int=deduct)
    print("Salary", readf["Salary"])
    print("Total Salary deduction", readf["Leave"])
