from Queue import Queue
from stack import Stack


def match(string):
    stack = Stack([])
    opening_braces = '([{'
    closing_braces = ')]}'
    for char in string:
        if char in opening_braces:
            stack.push(char)
        elif char in closing_braces:
            if stack.is_empty() or opening_braces[closing_braces.index(char)] != stack.pop():
                return False
    if not stack.is_empty():
        return False
    return True


def main():
    str1 = "([])"
    str2 = "( ( a )')"
    str3 = "(][)hello"
    # braces_dict = {'(': ')', '[': ']', '{': '}'}
    # stack = Stack([])
    # for char in str1:
    #     print(char)
    #     if char in braces_dict:
    #         stack.push(char)
    #         print("stack", stack)
    print(match(str2))
    print("End of main")


# Don't run main on import
if __name__ == "__main__":
    main()
