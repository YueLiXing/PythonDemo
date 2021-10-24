import os


mdFileTxt = open("README.md", encoding="utf-8").read()

needToDealPyFile = []
fileNames = os.listdir(os.path.join(os.getcwd(), 'LeeCode'))
for fileName in fileNames:
    if ".py" in fileName and fileName not in mdFileTxt:
        needToDealPyFile.append(fileName)
    if ".swift" in fileName and fileName not in mdFileTxt:
        needToDealPyFile.append(fileName)

if len(needToDealPyFile) == 0:
    print("All files in README.md!")
else:
    print("Some files are not in README.md", needToDealPyFile)
