class Solution:
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
            for i in range(-1,2):
                for j in range(-1,2):
                    tempC = board[centerY+j][centerX+i]
                    if tempC != ".":
                        if tempC in tempDict:
                            return False
                        else:
                            tempDict[tempC] = ""
                    
        return True
            
            
print(Solution().isValidSudoku([[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]))
