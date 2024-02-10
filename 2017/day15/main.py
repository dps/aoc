A,B = 699,124

c = 0
for _ in range(40000000):
    A = (A*16807) % 2147483647
    B = (B*48271) % 2147483647

    if (A & 0xffff) == (B & 0xffff):
        c += 1

print(c)

def genA():
    A = 699
    while True:
        A = (A*16807) % 2147483647
        if A % 4 == 0:
            yield A

def genB():
    B = 124
    while True:
        B = (B*48271) % 2147483647
        if B % 8 == 0:
            yield B

c = 0
ga,gb = genA(),genB()
for _ in range(5000000):
    a,b = next(ga),next(gb)
    if (a & 0xffff) == (b & 0xffff):
        c += 1
print(c)