import json

dict={
    "Food List": ["Wafer","Peanuts","Ice-Cream"],
    "Drink tuple":("Lassi","Soda","Energy"),
    "Number":987,
    "Float":25.25,
    "boolean": True,
}
# print("Python types into JSOn")
jsn=json.dumps(dict)
# print("After Converting")
print(jsn)
print("after convert",dict['Food List'])
