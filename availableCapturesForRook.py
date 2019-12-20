class Solution:
    def numRookCaptures(self, board: [[str]]) -> int:
        count = 0
        for indexI in range(8):
            tempB = board[indexI]
            for indexJ in range(8):
                tempCap = tempB[indexJ]
                if tempCap == "R":
                    # print(tempCap, indexI, indexJ)
                    for tempI in range(indexI+1, 8):
                        t = board[tempI][indexJ]
                        if t == '.':
                            continue
                        elif t == 'B':
                            break
                        elif t == 'p':
                            count += 1
                            break
                    for tempI in range(indexI-1, -1, -1):
                        t = board[tempI][indexJ]
                        if t == '.':
                            continue
                        elif t == 'B':
                            break
                        elif t == 'p':
                            count += 1
                            break
                    for tempJ in range(indexJ+1, 8):
                        t = board[indexI][tempJ]
                        if t == '.':
                            continue
                        elif t == 'B':
                            break
                        elif t == 'p':
                            count += 1
                            break
                    for tempJ in range(indexJ-1, -1, -1):
                        t = board[indexI][tempJ]
                        if t == '.':
                            continue
                        elif t == 'B':
                            break
                        elif t == 'p':
                            count += 1
                            break
                    return count
        return count


ret = Solution().numRookCaptures([
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "p", ".", ".", ".", "."],
    [".", ".", ".", "R", ".", ".", ".", "p"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "p", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."]
])
print(ret)
