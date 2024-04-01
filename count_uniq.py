from Queue import Queue
# from stack import Stack


def count_uniq(queue):
    count = 0
    last = None
    current = None
    while not queue.is_empty():
        current = queue.deq()
        if current == last:
            count += 1
        last = current
    return count


def main():
    queue = Queue(['h', 'e', 'e', 'e'])
    queue = Queue(['o', 'o', 'o', 'o', 'h', 'h'])
    print(count_uniq(queue))
    print("End of main")


# Don't run main on import
if __name__ == "__main__":
    main()
