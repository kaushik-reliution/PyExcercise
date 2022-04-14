#prob: You are given two lists of numbers and you need to find total of each of these list.
def cal_total(exp):# exp(function argument)
    """
    This function used to count expense of two different peoples.
    """
    total=0
    for i in exp:
        total=total+i
    return total # total(return value)

k1=[4500,6700,3200,5500]
k2=[7500,8000,900,2100]

ex_total=cal_total(k1)#exp1(poositional e=arguments) 2nd is Named Arguments like this(a=4,b=6)
ex2_total=cal_total(k2)

print("Expense k1 total is",ex_total)
print("expense k"
      "2 total is",ex2_total)
# total=0
# for i in exp1:
#     total=total+i
# print("Expense1 is ",total)
#
# total=0
# for i in exp2:
#     total=total+i
# print("Expense2 is ",total)
