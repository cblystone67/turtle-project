from Queue import Queue
from stack import Stack


def generate_binary_numbers(N):
    numbers = Queue([])
    stack = Stack()
    if N >= 1:
        generate_binary_numbers(N // 2)
        # numbers = N % 2
    print(N % 2, end='')
    # return numbers


def main():
    # print(generate_binary_numbers(24))
    N = 24
    generate_binary_numbers(N)
    print("\nEnd of main!")


if __name__ == '__main__':
    main()
