class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        toGuessResult = {}
        resultStepArr = []
        while True:
            # print("----------")
            toGuessResult.clear()
            resultStepArr.clear()
            flag = True
            for y in range(9):
                for x in range(9):
                    if board[y][x] == ".":
                        possibleResult = self.getValidSudokuResult(board, y, x)
                        if len(possibleResult) == 1:
                            board[y][x] = possibleResult[0]
                            flag = False
                        else:
                            toGuessResult[y*10+x] = {"r":possibleResult,"i":-1}
                            resultStepArr.append(y*10+x)
            if flag:
                break
        if len(toGuessResult) == 0: # Solved!
            return
        else:
            level = 0
            while level >= 0:
                p = resultStepArr[level]
                y = p//10
                x = p%10
                temp = toGuessResult[p]
                r = temp["r"]
                flag = False
                for i in range(temp["i"]+1, len(r)):
                    if self.checkCanSetSudoku(board, y, x, r[i]):
                        flag = True
                        board[y][x] = r[i]
                        temp["i"] = i
                        break
                # print(level, p, temp)
                if flag:
                    level += 1
                    if level == len(resultStepArr):
                        break
                else:
                    # print(level, p, temp)
                    temp["i"] = -1
                    board[y][x] = "."
                    level -= 1
            for k in toGuessResult:
                y = k//10
                x = k % 10
                v = toGuessResult[k]
                board[y][x] = v["r"][v["i"]]

        
    def getValidSudokuResult(self,board,y,x):
        tempArr = ['1','2','3','4','5','6','7','8','9']
        for indexY in range(9):
            tempC = board[indexY][x]
            if indexY != y and tempC != "." and tempC in tempArr:
                tempArr.remove(tempC)
        for indexX in range(9):
            tempC = board[y][indexX]
            if indexX != x and tempC != "." and tempC in tempArr:
                tempArr.remove(tempC)
        startX = x // 3
        startY = y // 3
        for indexY in range(startY*3, startY*3+3):
                for indexX in range(startX*3, startX*3+3):
                    tempC = board[indexY][indexX]
                    if tempC != "." and indexY != y and indexX != x and tempC in tempArr:
                        tempArr.remove(tempC)
        return tempArr

    def checkCanSetSudoku(self, board, y, x, val) -> bool:
        for indexY in range(9):
            tempC = board[indexY][x]
            if indexY != y and tempC == val:
                return False
        for indexX in range(9):
            tempC = board[y][indexX]
            if indexX != x and tempC == val:
                return False
        startX = x // 3
        startY = y // 3
        for indexY in range(startY*3, startY*3+3):
                for indexX in range(startX*3, startX*3+3):
                    tempC = board[indexY][indexX]
                    # print(tempC,val)
                    if indexY != y and indexX != x and tempC == val:
                        return False
        return True
        


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# Solution().solveSudoku(board)
# for val in board:
#     print(val)

board = [
    [".", ".", "9", "7", "4", "8", ".", ".", "."],
    ["7", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "2", ".", "1", ".", "9", ".", ".", "."],
    [".", ".", "7", ".", ".", ".", "2", "4", "."],
    [".", "6", "4", ".", "1", ".", "5", "9", "."], 
    [".", "9", "8", ".", ".", ".", "3", ".", "."], 
    [".", ".", ".", "8", ".", "3", ".", "2", "."], 
    [".", ".", ".", ".", ".", ".", ".", ".", "6"], 
    [".", ".", ".", "2", "7", "5", "9", ".", "."]]
Solution().solveSudoku(board)
for val in board:
    print(val)

# [
#     ["5","1","9","7","4","8","6","3","2"],
#     ["7","8","3","6","5","2","4","1","9"],
#     ["4","2","6","1","3","9","8","7","5"],
#     ["3","5","7","9","8","6","2","4","1"],
#     ["2","6","4","3","1","7","5","9","8"],
#     ["1","9","8","5","2","4","3","6","7"],
#     ["9","7","5","8","6","3","1","2","4"],
#     ["8","3","2","4","9","1","7","5","6"],
#     ["6","4","1","2","7","5","9","8","3"]
#     ]
