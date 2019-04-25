from collections import deque



class MinMaxStack:
    """
    Find Min/Max using a stack in O(1) time.
    Using Deque/Tuple

    """
    def __init__(self, op=min):
        self._stack = deque()
        self.op = op

    def is_empty(self):
        return len(self._stack) == 0

    def push(self, item):
        if len(self._stack) == 0:
            max_min = item
        else:
            max_min = self.op(item, self._stack[-1][1])
        self._stack.append((item, max_min))

    def pop(self):
        if len(self._stack) == 0:
            raise IndexError()
        return self._stack.pop()[0]

    def query(self):
        if len(self._stack) == 0:
            raise IndexError()
        return self._stack[-1][1]


def demo_max_stack():
    min_max_stack = MinMaxStack(op=max)
    nums = [0, -1, 8, -95, 89, -101, 54]
    for num in nums:
        min_max_stack.push(num)
    print(min_max_stack.query())


def demo_min_stack():
    min_max_stack = MinMaxStack()
    nums = [0, -1, 8, -95, 89, -101, 54]
    for num in nums:
        min_max_stack.push(num)
    print(min_max_stack.query())


if __name__ == '__main__':
    demo_max_stack()
    demo_min_stack()






