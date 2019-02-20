class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        ret = []
        lastArr = []
        for i in range(len(asteroids)-1,-1,-1):
            if len(lastArr) == 0:
                if asteroids[i] > 0:
                    ret.insert(0, asteroids[i])
                else:
                    lastArr.append(asteroids[i])
            else:
                if asteroids[i] < 0:
                    lastArr.append(asteroids[i])
                else:
                    # 开始碰撞
                    flag = False
                    for index in range(len(lastArr)-1,-1,-1):
                        if abs(lastArr[index]) > asteroids[i]:
                            flag = False
                            break
                        elif abs(lastArr[index]) == asteroids[i]: # 同归于尽
                            lastArr.pop(index)
                            flag = False
                            break
                        else:
                            flag = True
                            lastArr.pop(index)
                    if flag:
                        ret.insert(0,asteroids[i])
        for index in range(len(lastArr)):
            ret.insert(0,lastArr[index])
        return ret
                            
            
print(Solution().asteroidCollision([5, 10, -5]))
print(Solution().asteroidCollision([-2, -1, 1, 2]))
print(Solution().asteroidCollision([-2, 2, -1, 1]))


