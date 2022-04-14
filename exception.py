x=input("Enter 1st number")
y=input("Enter 2nd number")
try:
    z= int(x) / int(y)
except Exception as e:
    print("Name of error",type(e).__name__)# Here u r able to ger name of error
    print("Division by zero is Exception ")
    z=None
print("Division is",z)
