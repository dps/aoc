from utils import *
input = [i.strip() for i in open("input.txt","r").readlines()]

def p1():
    pwd = ""
    files = defaultdict(int)
    for line in input:
        if line.startswith("$"):
            if line.split(" ")[1] == "cd":
                next_dir = line.split(" ")[2]
                if next_dir == "..":
                    paths = pwd.split("/")
                    paths.pop()
                    pwd = "/".join(paths)
                elif next_dir == "/":
                    pwd = "/"
                else:
                    if pwd == "/":
                        pwd = "/" + next_dir
                    else:
                        pwd = pwd + "/" + next_dir
        if re.match(r'^\d+', line):
            files[pwd + "/" + line.split(" ")[1].strip()] = int(line.split(" ")[0])

    acc = defaultdict(int)
    for file,size in files.items():
        p = ""
        for part in file.split("/")[1:-1]:
            p += "/" + part
            acc[p] += size
    
    score = 0
    for dirs, size in acc.items():
        if size <= 100000:
            print(dirs)
            score += size
    print(score)



def part1():
    pwd = '/'
    phase = ""
    files = defaultdict(int)
    for line in input:
        match line[0]:
            case '$':
                cmds = line.split(" ")
                match cmds[1]:
                    case "cd":
                        match cmds[2]:
                            case "..":
                                dirs = pwd.split("/")
                                dirs.pop()
                                pwd = "/".join(dirs)
                            case "/":
                                pwd = "/"
                            case _:
                                next_dir = cmds[2]
                                if pwd != "/":
                                    pwd = pwd + "/" + next_dir
                                else:
                                    pwd = next_dir
                    case "ls":
                        phase = "ls"
            case _:
                if phase == "ls":
                    toks = line.split(" ")
                    if toks[0].isdigit():
                        files[pwd + "/" + toks[1]] = int(toks[0])
                else:
                    assert(False)
    print(files)
    acc = defaultdict(int)
    
    for k,v in files.items():
        k = k[1:]
        print("aaa ", k)
        for dir in k.split("/")[:-1]:
            print("aa ", dir)
            acc[dir] += v
    score = 0
    for dir, size in acc.items():
        print(dir," ",size)
        if size <= 100000:
            print("**")
            score += size

    print(score)

def part2():
    pwd = ""
    files = defaultdict(int)
    for line in input:
        if line.startswith("$"):
            if line.split(" ")[1] == "cd":
                next_dir = line.split(" ")[2]
                if next_dir == "..":
                    paths = pwd.split("/")
                    paths.pop()
                    pwd = "/".join(paths)
                elif next_dir == "/":
                    pwd = "/"
                else:
                    if pwd == "/":
                        pwd = "/" + next_dir
                    else:
                        pwd = pwd + "/" + next_dir
        if re.match(r'^\d+', line):
            files[pwd + "/" + line.split(" ")[1].strip()] = int(line.split(" ")[0])

    acc = defaultdict(int)
    for file,size in files.items():
        p = ""
        for part in file.split("/")[:-1]:
            p += "/" + part
            acc[p] += size

    target = 30000000 - (70000000 - acc["/"])
    print(target)
    big_enough = [size for (file, size) in acc.items() if size >= target]
    big_enough.sort()
    print(big_enough)

if __name__ == '__main__':
    #p1()
    part2()