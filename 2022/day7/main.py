from utils import *
input = [i.strip() for i in open("input.txt","r").readlines()]

def part1():
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
        print(dirs)
        if size <= 100000:
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
    part1()
    #part2()