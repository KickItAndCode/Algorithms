class MinStack:
    # @param x, an integer


def __init__(self):
    # the stack it self
    self.stack = []
    self.minS = []
# @return an integer


def push(self, x):
    n = len(self.stack)
    if n == 0:
        self.minS.append(x)
    else:
        lastmin = self.minS[-1]
        if x <= lastmin:
            self.minS.append(x)
    self.stack.append(x)
# @return nothing


def pop(self):
    if len(self.stack) > 0 and self.stack.pop() == self.minS[-1]:
        self.minS.pop()
# @return an integer


def top(self):
    return self.stack[-1]


# @return an integer
def getMin(self):
    return self.minS[-1]


class MinStack:
    def __init__(self):
        self.data = [(None, float('inf'))]

    def push(self, x: 'int') -> 'None':
        self.data.append((x, min(x, self.data[-1][1])))

    def pop(self) -> 'None':
        if len(self.data) > 1:
            self.data.pop()

    def top(self) -> 'int':
        return self.data[-1][0]

    def getMin(self) -> 'int':
        return self.data[-1][1]
