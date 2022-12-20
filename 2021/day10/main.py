from utils import *

input = [i for i in open("input.txt","r").readlines()]

def part1():
    score = 0
    stack = deque([])
    for line in input:
        illegal = 0
        for ch in line:
            if ch in "([{<":
                stack.appendleft(ch)
            elif ch in ")]}>":
                opened_by = stack.popleft()
                if ch == ">" and opened_by != "<":
                    illegal = 25137
                    break
                if ch == ")" and opened_by != "(":
                    illegal = 3
                    break
                if ch == "]" and opened_by != "[":
                    illegal = 57
                    break
                if ch == "}" and opened_by != "{":
                    illegal = 1197
                    break
        score += illegal
    print(score)
    return score

SCORES = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

def part2():
    score = 0
    completions = []
    for line in input:
        illegal = False
        stack = deque([])
        for ch in line:
            if ch in "([{<":
                stack.appendleft(ch)
            elif ch in ")]}>":
                opened_by = stack.popleft()
                if ch == ">" and opened_by != "<":
                    illegal = True
                    break
                if ch == ")" and opened_by != "(":
                    illegal = True
                    break
                if ch == "]" and opened_by != "[":
                    illegal = True
                    break
                if ch == "}" and opened_by != "{":
                    illegal = True
                    break
        if not illegal:
            ll = [SCORES[x] for x in stack]
            s = 0
            for l in ll:
                s *= 5
                s += l
            completions.append(s)
    completions=sorted(completions)
    print(completions[len(completions)//2])
    return completions[len(completions)//2]

if __name__ == '__main__':
    assert(part1() == 411471)
    assert(part2() == 3122628974)
