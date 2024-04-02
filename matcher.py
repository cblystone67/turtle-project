from Queue import Queue
from stack import Stack


def match(string):
    braces_dict = {'(': ')', '[': ']', '{': '}'}
    stack = Stack([])
    for char in string:
        if char in braces_dict.keys():
            stack.push(char)
        elif char in braces_dict.values():
            if not stack or braces_dict[stack.pop()] != char:
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
