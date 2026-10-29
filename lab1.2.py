transaction =[ ["bread", "milk"],
        ["bread","butter", "milk"],
        ["bread", "butter"],
        ["milk"],
        ["bread", "milk","eggs"],
]

total = len(transaction)

bread_count=0
butter_count=0
both_count =0

for items in transaction:
    if "bread" in items:
        bread_count+=1

    if"butter" in items:
        butter_count+=1

    if "bread" in items and "butter" in items:
        both_count+=1

support = both_count / total

confdence = both_count / bread_count


print("the total transaction is: ", total)
print("the bread transaction is: ",bread_count)
print("the butter transaction is:", butter_count)
print("the bread and butter transaction are: ",both_count)

print("support is ", support)
print("confdence is ", confdence)

print ("\nthe support percentage = ", support*100,"%")
print("confidence percentage = ", confdence*100,"%")