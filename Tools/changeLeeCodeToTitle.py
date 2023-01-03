
import sys
engTitle = "er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof"


tempArr = engTitle.split("-")
resultArr = []
for temp in tempArr:
    if len(temp) >= 1 and len(resultArr):
        temp = temp.capitalize()
    resultArr.append(temp)


print("".join(resultArr)+".py")
print("".join(resultArr)+".swift")
