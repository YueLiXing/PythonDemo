
engTitle = "add-digits"

tempArr = engTitle.split("-")
resultArr = []
for temp in tempArr:
    if len(temp) > 1 and len(resultArr):
        temp = temp.capitalize()
    resultArr.append(temp)


print("".join(resultArr)+".py")


# import collections

# temp = collections.OrderedDict()
# temp[1] = 1
# temp[2] = 2
# temp[3] = 3
# print(temp)
# temp.popitem(False)
# # temp[2] = 22
# # print(temp)
# # temp.move_to_end(1)
# print(temp)

# temp = 100
# while True:
#     ret = temp*52
#     ret = ret//10
#     if ret%10 ==9:
#         ret = ret //10
#         if ret %10 == 3:
#             print(temp, temp*52)
#             break
#     temp += 1
#     if temp > 200:
#         print("error")
