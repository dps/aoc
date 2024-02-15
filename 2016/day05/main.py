
import hashlib

door = open("input","r").read().strip().encode()

def part1(door):
    password = ""

    i = 0
    while len(password) < 8:
        h = hashlib.md5(door + str(i).encode()).hexdigest()
        if i % 10000 == 0: # Be extra proud of your solution if it uses a cinematic "decrypting" animation.
            print(f"\r{password}{h[0:8-len(password)]}",end="")

        if h[0:5] == "00000":
            password += h[5]
        i += 1

    print(" -->", password)


def part2(door):
    password = list("........")
    seen = set()

    i = 0
    while len(seen) < 8:
        h = hashlib.md5(door + str(i).encode()).hexdigest()
        if i % 10000 == 0: # Be extra proud of your solution if it uses a cinematic "decrypting" animation.
            p = [h if p=='.' else p for (h,p) in zip(list(h), password)]
            print(f"\r{''.join(p)}",end="")
        if h[0:5] == "00000":
            try:
                pos = int(h[5])
                ch = h[6]
                if pos not in seen:
                    password[pos] = ch
                    seen.add(pos)
            except:
                pass
        i += 1

    print(" -->", "".join(password))

part1(door)
part2(door)