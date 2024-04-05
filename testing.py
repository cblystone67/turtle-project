from Queue import Queue
from stack import Stack


def decimalToBinary(num):
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')


def main():
    number = 39
    decimalToBinary(number)


main()


def match(string):
    stack = Stack()
    opening_braces = '([{'
    closing_braces = ')]}'

    for char in string:
        if char in opening_braces:
            stack.push(char)
        elif char in closing_braces:
            # If stack is empty or the top of the stack doesn't match the corresponding opening brace
            if stack.is_empty() or opening_braces[closing_braces.index(char)] != stack.pop():
                return False

    # If there are unmatched opening braces left in the stack
    if not stack.is_empty():
        return False

    return True


# Test the function
print(match("()[]{}"))  # True
print(match("([{}])"))  # True
print(match("([)]"))    # False
