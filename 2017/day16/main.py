
D = open("input","r").read().strip().split(",")

lineup = list(chr(ord('a')+x) for x in range(16))
seen = {}
idx = {}
i = 0
while True:
    for move in D:
        do = move[0]
        if do == 's':
            num = int(move[1:])
            l,r = lineup[-num:], lineup[0:16-num]
            lineup = [*l,*r]
        if do == 'x':
            l,r = list(map(int, move[1:].split('/')))
            t = lineup[r]
            lineup[r] = lineup[l]
            lineup[l] = t
        if do == 'p':
            l,r = move[1:].split('/')
            pl,pr = lineup.index(l),lineup.index(r)
            t = lineup[pr]
            lineup[pr] = lineup[pl]
            lineup[pl] = t

    line = "".join(lineup)
    if i == 0:
        print(line)
    if line in seen:
        print(idx[1000000000 % i])
        break
    i += 1
    seen[line] = i
    idx[i] = line



