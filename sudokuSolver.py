class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[j][i] == ".":
                    print(self.getValidSudokuResult(board, i, j))
        # print(self.isValidSudoku(board))
    def getValidSudokuResult(self,board,i,j):
        tempDict = {"1":"","2":"","3":"","4":"","5":"","6":"","7":"","8":"","9":""}
        for indexI in range(9):
            tempC = board[indexI][j]
            if indexI != i and tempC != "." and tempC in tempDict:
                del tempDict[tempC]
        for indexJ in range(9):
            tempC = board[i][indexJ]
            if indexJ != j and tempC != "." and tempC in tempDict:
                del tempDict[tempC]
        centerX = 1
        centerY = 1
        if 0 <= i <= 2:
            centerX = 1
        elif 3 <= i <= 5:
            centerX = 4
        else:
            centerX = 7
        if 0 <= j <= 2:
            centerY = 1
        elif 3 <= j <= 5:
            centerY = 4
        else:
            centerY = 7
        for indexI in range(-1, 2):
                for indexJ in range(-1, 2):
                    tempC = board[centerY+indexJ][centerX+indexI]
                    if tempC != "." and centerY+indexJ != j and centerX+indexI != i and tempC in tempDict:
                        del tempDict[tempC]
        return tempDict.keys()
        

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            tempDict = {}
            for j in range(9):
                tempC = board[i][j]
                if tempC != ".":
                    if tempC in tempDict:
                        return False
                    else:
                        tempDict[tempC] = "1"
            tempDict.clear()
        for i in range(9):
            tempDict = {}
            for j in range(9):
                tempC = board[j][i]
                if tempC != ".":
                    if tempC in tempDict:
                        return False
                    else:
                        tempDict[tempC] = "1"
            tempDict.clear()
        bufferArr = [
            {
                "x": 1,
                "y": 1
            },
            {
                "x": 1,
                "y": 4
            },
            {
                "x": 1,
                "y": 7
            },
            {
                "x": 4,
                "y": 1
            },
            {
                "x": 4,
                "y": 4
            },
            {
                "x": 4,
                "y": 7
            },
            {
                "x": 7,
                "y": 1
            },
            {
                "x": 7,
                "y": 4
            },
            {
                "x": 7,
                "y": 7
            }
        ]
        for temp in bufferArr:
            centerX = temp["x"]
            centerY = temp["y"]
            tempDict = {}
            for i in range(-1, 2):
                for j in range(-1, 2):
                    tempC = board[centerY+j][centerX+i]
                    if tempC != ".":
                        if tempC in tempDict:
                            return False
                        else:
                            tempDict[tempC] = ""

        return True


print({1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}.keys())
Solution().solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
