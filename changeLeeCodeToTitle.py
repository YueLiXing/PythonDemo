
engTitle = "contains-duplicate-iii"

tempArr = engTitle.split("-")
resultArr = []
for temp in tempArr:
    if len(temp) > 1 and len(resultArr):
        temp = temp.capitalize()
    resultArr.append(temp)


print("".join(resultArr)+".py")


import collections

temp = collections.OrderedDict()
temp[1] = 1
temp[2] = 2
temp[3] = 3
print(temp)
temp.popitem(False)
# temp[2] = 22
# print(temp)
# temp.move_to_end(1)
print(temp)

