
pattern = open("input","r").read().strip()

grid = []
grid.append(pattern)
for k in range(400000-1):
    a,b,c = None, None, None
    patt = "."+grid[-1]+"."
    row = ""
    for i in range(len(pattern)):
        a,b,c = patt[i],patt[i+1],patt[i+2]
        if a == "^" and b == "^" and c == ".":
            row += "^"
        elif a == "." and b == "^" and c == "^":
            row += "^"
        elif a == "^" and b == "." and c == ".":
            row += "^"
        elif a == "." and b == "." and c == "^":
            row += "^"
        else:
            row += "."
    grid.append(row)
    if k == 38: #part 1
        print(sum([sum(1 for a in row if a == '.') for row in grid]))

print(sum([sum(1 for a in row if a == '.') for row in grid]))