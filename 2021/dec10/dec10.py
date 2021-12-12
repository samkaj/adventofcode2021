SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137, "(": 1, "[": 2, "{": 3, "<": 4}
CLOSER = {")": "(", "]": "[", "}": "{", ">": "<"}


def main():
    # get input
    with open("2021/dec10/input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    corrupt_score = 0
    autocomplete_score = []
    for line in lines:
        scores = get_score(line)
        corrupt_score += scores[0]
        if scores[1] > 0:
            autocomplete_score.append(scores[1])
    print(
        f"Corruption score: {corrupt_score}, Autocomplete score: {median(autocomplete_score)}"
    )


def median(scores):
    mid = int((len(scores) - 1) / 2)
    scores.sort()
    return scores[mid]


def get_score(line):
    stack = []
    corrupt_score = 0
    corrupt = False
    for c in line:
        if c in "}])>":
            opener = stack.pop()
            if opener != CLOSER[c] and corrupt_score == 0:
                corrupt_score += SCORE[c]
                corrupt = True
        else:
            stack.append(c)

    autocomplete_score = 0
    if not corrupt:
        # NO idea why I need -1 as stop??? oh well
        for i in range(len(stack) - 1, -1, -1):
            autocomplete_score *= 5
            autocomplete_score += SCORE[stack[i]]
    return corrupt_score, autocomplete_score


if __name__ == "__main__":
    main()
