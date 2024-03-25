from Queue import Queue
from stack import Stack


def flip(stack):
    f = Stack()
    while not stack.is_empty():
        f.push(stack.pop())
    return f


def main():
    stack = Stack(['h', 'e', 'l', 'l', 'o'])
    flip(stack).print()
    print("End of main")


# Don't run main on import
if __name__ == "__main__":
    main()
