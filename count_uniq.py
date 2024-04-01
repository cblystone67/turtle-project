from Queue import Queue
# from stack import Stack


def count_uniq(q):
    len = 0  # Num of Char
    count = 0
    last = None  # last char
    current = None
    while not q.is_empty():
        current = q.deq()
        count = 1
        if current == last:
            len += 1
        last = current
    return len


def main():
    queue = Queue(['h', 'e', 'e', 'e', 'l', 'l', 'o'])
    queue1 = Queue(['o', 'o', 'o', 'o', 'h', 'h'])

    print(count_uniq(queue))
    print("End of main")


# Don't run main on import
if __name__ == "__main__":
    main()
