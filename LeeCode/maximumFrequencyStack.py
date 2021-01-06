import collections


class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)

    def pop(self):
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x


        # self.cacheCount.values
        # Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(5)
# obj.push(7)
# obj.push(5)
# obj.push(7)
# obj.push(4)
# obj.push(5)
# print(obj.pop())
# print(obj.pop())
# print(obj.pop())
# print(obj.pop())

# ["FreqStack", "push", "push", "push", "push", "push", "push", "push", "push", "push",
#     "push", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop"]
# , [1], [6], [1],
#     [5], [], [], [], [], [], [], [], [], [], []]

obj = FreqStack()
obj.push(5)
obj.push(1)
obj.push(2)
obj.push(5)
obj.push(5)
obj.push(5)
obj.push(1)
obj.push(6)
obj.push(1)
obj.push(5)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
