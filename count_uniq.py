from Queue import Queue
# from stack import Stack


def count_uniq(q):
    len = 0
    if q.is_empty():
        len = 0
    elif q.size() == 1:
        len = 1
    current_count = 1
    current_char = q.deq()
    next_char = None
    while not q.is_empty():
        next_char = q.deq()
        if current_char == next_char:
            current_count += 1
        else:
            current_char = next_char
            if current_count > len:
                len = current_count
            current_count = 1
        if q.is_empty():
            if current_count > len:
                len = current_count
        q.size()
    return len


def main():
    # q = Queue(['o', 'o', 'o', 'o', 'h', 'h', 'h', 'h',
    #           'h', 'a', 'a', 'e', 'e', 'e', 'e', 'e', 'e'])
    # q1 = Queue(['h', 'e', 'l', 'l', 'o'])
    q2 = Queue(['m'])
    # que = Queue()
    # for i in range(4):
    #     que.enq('oe')
    # q3 = Queue(['o', 'o', 'o', 'o', 'h', 'h', 'e', 'e', 'e', 'e'])
    print(count_uniq(q2))
    print("End of main")


# Don't run main on import
if __name__ == "__main__":
    main()
