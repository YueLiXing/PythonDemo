
engTitle = "reverse-linked-list-ii"

tempArr = engTitle.split("-")
resultArr = []
for temp in tempArr:
    if len(temp) > 1 and len(resultArr):
        temp = temp.capitalize()
    resultArr.append(temp)


print("".join(resultArr)+".py")
