from Queue import Queue
from stack import Stack


def generate_binary_numbers(N):
    numbers = Queue([])
    stack = Stack()
    binary_power = 0
    binary_num = 0
    counter = 0
    while binary_num <= N:
        binary_num = 2 ** binary_power
        stack.push(binary_num)
        if binary_num > N:
            stack.pop()
        binary_power += 1
    count = stack.pop()
    numbers.enq('1')
    while not stack.is_empty():
        current_pop = stack.pop()
        if current_pop + count >= N:
            numbers.enq('0')
        elif current_pop + count <= N:
            numbers.enq('1')
        else:
            numbers.enq('0')

    return numbers


def main():
    # print(generate_binary_numbers(24))
    N = 2

    print(generate_binary_numbers(N))
    print("End of main!")


if __name__ == '__main__':
    main()
