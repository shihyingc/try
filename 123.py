from random import choice

coin=["Head","Tail"]
list_result=[]

while list_result.count("Head")<3:
    list_result.append(choice(coin))

print(list_result)
print("you've tried %i times" %len(list_result))