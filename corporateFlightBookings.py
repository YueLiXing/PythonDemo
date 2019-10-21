class Solution:
    def corpFlightBookings(self, bookings: [[int]], n: int) -> [int]:
        ret = []
        for i in range(n):
            ret.append(0)
        for book in bookings:
            begin = book[0]
            end = book[1]
            count = book[2]
            for i in range(begin-1,end):
                ret[i] = ret[i]+count
        return ret

r = Solution().corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]],5)
print(r)