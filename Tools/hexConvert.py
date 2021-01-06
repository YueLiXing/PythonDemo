def change(num, hexNum=16)-> str:
    if hexNum > 36 or num < 0:
        raise(BaseException("数据异常"))
    ret = ""
    temp = 1
    cache = {}
    for i in range(10):
        cache[i] = str(i)
    for i in range(ord('A'), ord('Z')+1):
        cache[i-ord('A')+10] = chr(i)

    while num > 0:
        c = num % hexNum
        ret = cache[c]+ret
        num //= hexNum
        # print(num, c)
    return ret


n = -115792089237316195423570985008687907853269984665640564039457584007913129639935

try:
    print(change(n, 16))
except BaseException as identifier:
    print(identifier)

# print(("%c" % chr(ord('A')+1)))
