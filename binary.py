from Queue import Queue
from stack import Stack


def generate_binary_numbers(N):
    numbers = Queue([])
    stack = Stack()
    if N == 0:
        numbers.enq("0")
        return numbers
    while N > 0:
        remainder = N % 2
        numbers.enq(remainder)
        N //= 2
    while not numbers.is_empty():
        stack.push(numbers.deq())
    while not stack.is_empty():
        numbers.enq(stack.pop())
    return numbers


def main():
    num = 0

    binary_num = generate_binary_numbers(num)
    print(binary_num)

    print("End of main!")


if __name__ == '__main__':
    main()
