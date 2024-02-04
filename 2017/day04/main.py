D = [i.strip() for i in open("input", "r").readlines()]

p1, p2 = 0, 0
for line in D:
    words, grams = set(), set()
    bad1, bad2 = False, False
    for word in line.split():
        if word in words:
            bad1 = True
        if tuple(sorted(word)) in grams:
            bad2 = True
        grams.add(tuple(sorted(word)))
        words.add(word)
    if not bad2:
        p2 += 1
    if not bad1:
        p1 += 1

print(p1, p2)
