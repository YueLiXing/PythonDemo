# class Solution:
#     def removeInvalidParentheses(self, s: str) -> [str]:
#         result = []
#         return result

coustArr = []
count = 3
# count = int(input("count"))
# for i in range(count):
#     t = input("")
#     coustArr.append(t.split(' '))
coustArr.append([2, 3, 1])
coustArr.append([6, 9, 2])
coustArr.append([0, 5, 1])
# 按照结束时间升序排列
coustArr.sort(key=lambda s: s[1])
print(coustArr)

result = 0
time = 0
left = 0
while left < count:
    temp = 0
    for index in range(left, count):
        task = coustArr[index]
    # for task in coustArr:
        if task[0] <= time and time < task[1]:
            temp += task[2]
        if time >= task[1]:
            # 当前时间大于等于当前任务的结束时间时，左边的游标向右移动
            left = index+1
    time += 1
    result = max(result, temp)
print(result)
