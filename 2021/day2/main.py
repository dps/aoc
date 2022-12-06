input = [i.strip() for i in open("input.txt","r").readlines()]

pos = 0
depth = 0
aim = 0
for x in input:
    cmd = x.split(" ")[0]
    n = int(x.split(" ")[1])
    match (cmd):
        case "forward":
            pos = pos + n
            depth = depth + aim * n
        case "down":
            aim = aim + n
        case "up":
            aim = aim - n
  
print(pos * depth)
