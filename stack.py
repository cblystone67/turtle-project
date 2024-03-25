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


def main():
    s = Stack()
    s2 = Stack()
    for i in range(1, 5):
        s.push(i)
    print("This is s", s)
    for i in range(s.size()):
        item = s.pop()
        s2.push(item)

    print("S2", s2)
    s = Stack([1, 2, 3, 4])
    flipped = flip(s)
    print("this is flipped", flipped)

    q_orig = Queue([2, 3, 4, 5])
    q_new = Queue([])
    s = Stack()
    while not q_orig.is_empty():
        s.push(q_orig.deq())
        q_new.enq(s.pop())
    print("this is s", s)
    print("This is q_new", q_new)


# Don't run main on import
if __name__ == "__main__":
    main()
