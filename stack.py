# STACK IMPLEMENTATION
# DO NOT MODIFY
from Queue import Queue


class Stack(object):
    def __init__(self, list=None):
        if list is None:
            list = []
        self.stack = list

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def push(self, data=None):
        self.stack.append(data)

    def print(self):
        print(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack = []

    def __str__(self):
        return self.stack.__str__()

    def __repr__(self):
        return self.stack.__repr__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.stack == other.stack
        return False

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_empty():
            raise StopIteration
        return self.pop()

    def size(self):
        return len(self.stack)


def flip(stack):
    flipped_stack = Stack()
    for i in range(stack.size()):
        item = stack.pop()
        flipped_stack.push(item)
    return flipped_stack


def reverse(q_orig):
    q_new = Queue([])
    s = Stack()
    for i in q_orig:
        s.push(i)
    while not s.is_empty():
        q_new.enq(s.pop())
    return q_new


def flip(stack):
    f = Stack()

    while not stack.is_empty():
        f.push(stack.pop())
    return f


def main():
    # s = Stack()
    # s2 = Stack()
    # for i in s:
    #     s.push(i)
    # print("This is s", s)
    # for i in range(s.size()):
    #     item = s.pop()
    #     s2.push(item)
    # print("S2", s2)
    # s = Stack(['hello'])
    # flipped = flip(s)
    # print("this is flipped", flipped)
    # list = '12345'
    # q_orig = Queue([])
    # q_new = Queue([])
    # s = Stack()
    # for i in list:
    #     print("i", i)
    #     s.push(i)
    #     print("s", s)
    # for i in range(s.size()):
    #     print(i)
    #     q_new.enq(s.pop())

    # print("q_new", q_new)
    q_orig = []
    print(reverse(q_orig))
    print("End of main")
    stack = Stack(['h', 'e', 'l', 'l', 'o'])
    print(flip(stack))


# Don't run main on import
if __name__ == "__main__":
    main()
