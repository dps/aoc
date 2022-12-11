from utils import *
input = [i.strip() for i in open("input.txt","r").readlines()]

def operate(old, op):
    old = eval("old " + op)
    return old

def solve(part, rounds):
    divisors = 1
    monkey = 0
    m = defaultdict(lambda : {})
    for line in input:
        if line.startswith("Monkey"):
            monkey = ints(line)[0]
        else:
            match line.strip().split(" ")[0]:
                case "Starting":
                    m[monkey]["starting"] = ints(line)
                    m[monkey]["inspected"] = 0
                case "Operation:":
                    m[monkey]["op"] = line.split("new = old")[1].strip()
                case "Test:":
                    m[monkey]["div"] = ints(line)[0]
                    divisors *= m[monkey]["div"]
                case "If":
                    if line.strip().split(" ")[1] == "true:":
                      m[monkey]["true"] = ints(line)[0]
                    else:
                      m[monkey]["false"] = ints(line)[0]
    for _ in range(rounds):
        for monk in range(monkey + 1):
            M = m[monk]
            for item in m[monk]["starting"]:
                m[monk]["inspected"] += 1
                l = operate(item, M["op"])
                if part == 1:
                    l = l // 3
                else:
                    l = l % divisors
                throw_to = -1
                if (l % M["div"]) == 0:
                    # throw
                    throw_to = M["true"]
                else:
                    throw_to = M["false"]
                items = deepcopy(m[throw_to]["starting"])
                items.append(l)
                m[throw_to]["starting"] = items
            m[monk]["starting"] = []

    l = [i["inspected"] for k,i in m.items()]
    l.sort(reverse=True)
    print(l[0] * l[1])

if __name__ == '__main__':
    solve(1, 20)
    solve(2, 10000)