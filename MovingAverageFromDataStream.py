# Moving Average from Data Stream
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Example 1:

# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1 // return 1.00000
# m.next(10) = (1 + 10) / 2 // return 5.50000
# m.next(3) = (1 + 10 + 3) / 3 // return 4.66667
# m.next(5) = (10 + 3 + 5) / 3 // return 6.00000


class MovingAverage:
    """
    @param: size: An integer
    """

    def __init__(self, size):
        # do intialization if necessary
        self.size = size
        self.window = [] * size
        self.sum = 0
    """
    @param: val: An integer
    @return:  
    """

    def next(self, val):

        if len(self.window) == self.size:
            self.sum -= queue.pop(0)

        self.window.append(val)
        self.sum += val
        return self.sum / len(self.window)

        # write your code here


m = MovingAverage(3)
print(m.next(1))  # = 1
print(m.next(10))  # = (1 + 10) / 2  # returns 5.5
