import os


mdFileTxt = open("README.md", encoding="utf-8").read()

needToDealPyFile = []
for fileName in os.listdir(os.getcwd()):
    if ".py" in fileName and fileName not in mdFileTxt:
        needToDealPyFile.append(fileName)
    if ".swift" in fileName and fileName not in mdFileTxt:
        needToDealPyFile.append(fileName)
print(needToDealPyFile)

