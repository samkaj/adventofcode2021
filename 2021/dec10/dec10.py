def main():
    # get input
    with open("2021/dec10/test.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    
    score = 0
    for line in lines:
        score += syntax_score(line)

    print(score)


def syntax_score(line):
    stack = []
    for c in line:
        if is_starting(c):
            stack.append(c)
        elif is_closing(c):
            if not is_correct_closing(c, stack.pop()):
                return get_score(c)
    return 0

def line_is_corrupted(line):
    return False

def get_score(c):
    if c == ')':
        return 3
    elif c == ']':
        return 57
    elif c == '}':
        return 1197
    elif c == '>':
        return 25137

def is_starting(c):
    return (
        c == '(' or
        c == '{' or
        c == '[' or
        c == '<'
    )

def is_closing(c):
    return (
        c == ')' or
        c == ']' or
        c == '}' or
        c == '>'
    )

def get_closing(c):
    if c == '(':
        return ')'
    elif c == '{':
        return '}'
    elif c == '[':
        return ']'
    elif c == '<':
        return '>'

def get_opening(c):
    if c == ')':
        return '('
    elif c == '}':
        return '{'
    elif c == ']':
        return '['
    elif c == '>':
        return '<'

def is_correct_closing(c, closing):
    return closing == get_closing(c)

if __name__ == "__main__":
    main()
