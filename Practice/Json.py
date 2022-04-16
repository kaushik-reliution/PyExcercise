#Convert Python dictionary into a JSON formatted String
import json

def jsn_response(result):
    print("Convert python dictionary into JSON formatted string")
    return_str=json.dumps(result)
    print(result)

org_dict={
    "name": "Original String",
    "function": "jsn response",
    "json dumps": "covnert dict into json string",
}
jsn_response(org_dict)
