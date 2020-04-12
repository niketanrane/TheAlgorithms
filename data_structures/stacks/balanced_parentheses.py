from data_structures.stacks.stack import Stack

bracket_map = {
    '(': ')',
    '{': '}',
    '[': ']'
}

def balanced_parentheses(example):
    is_balanced = True
    stack = Stack()
    for char in example:
        if char in ['(', '{', '[']:
            stack.push(char)
        elif char in [')', '}', ']']:
            # print(stack)
            if stack.is_empty() or bracket_map[stack.pop()] != char:
                is_balanced = False
                break

    return is_balanced and stack.is_empty()


if __name__ == "__main__":
    examples = ["((()))", "((())", "(()))", "()[]{}", "()", "", "(]", "{[]}"]
    print("Balanced parentheses demonstration:\n")
    for example in examples:
        print(example + ": " + str(balanced_parentheses(example)))
