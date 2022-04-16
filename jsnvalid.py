import json
def validate(jsndata):
    try:
        json.loads(jsndata)
    except ValueError as err:
        return False
    return True

invalid="""{"Name": "Keval","Salary": "10000","Email": "keval123@sample.com",}"""
check=validate(invalid)
print("Valid json string? --- ",check)
valid="""{"Name": "Keval","Salary": "10000","Email": "keval123@sample.com"}"""
check=validate(valid)
print("valida json string:-  ",check,"\n",valid)