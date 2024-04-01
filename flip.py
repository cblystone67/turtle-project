from Queue import Queue
from stack import Stack


def flip(queue):
    f = Stack()
    while not queue.is_empty():
        f.push(queue.deq())
    while not f.is_empty():
        queue.enq(f.pop())

    return queue


def main():
    queue = Queue(['h', 'e', 'l', 'l', 'o'])
    flip(queue).print()
    print("End of main")


# Don't run main on import
if __name__ == "__main__":
    main()
