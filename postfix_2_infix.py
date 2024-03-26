from Queue import Queue
from stack import Stack


def postfix_2_infix(queue):
    s = Stack([])
    while not queue.is_empty():
        c = queue.deq()
        if c in "+-/*":
            op2 = s.pop()
            op1 = s.pop()
            s.push(op1 + c + op2)
        else:
            s.push(c)

    return s.pop()


def main():
    queue = Queue(['1', '2', '+'])
    queue2 = Queue(['5', '4', '*', '7', '+'])
    queue3 = Queue(['1', '2', '+'])
    print(postfix_2_infix(queue))
    print("End of Main")


if __name__ == "__main__":
    main()
