# Part 2 solution by analysis

The program computes the sum of the factors of a big number (part 2) or small number (part 1)

# The program
```
a,b,c,d,ip,f = 0
0 1 2 3 4  5
-1 #ip 4
0 addi 4 16 4       # jmp 17  #ip = ip + 16 (ip == 0 on this line)
1 seti 1 1 1        # b = 1
2 seti 1 7 3        # d = 1
3 mulr 1 3 2        # c = b * d
4 eqrr 2 5 2        # c = f == c
5 addr 2 4 4        # jmp (6+c)  [i.e. 6 iff b*d != c, else 7]
6 addi 4 1 4        # jmp 8
7 addr 1 0 0        # a = a + b
8 addi 3 1 3        # c = c + 1
9 gtrr 3 5 2        # c = d > f
10 addr 4 2 4       # jmp (11+c) [i.e. 11 iff d <= f, 12 iff d>f]
11 seti 2 3 4       # jmp 3
12 addi 1 1 1       # b=b+1
13 gtrr 1 5 2       # c = b > f
14 addr 2 4 4       # jmp 15+c [i.e. 15 if b<=f, 16 if b>f]
15 seti 1 6 4       # jmp 2
16 mulr 4 4 4       # jmp 256+1 i.e. terminate ip = ip * ip
# Compute big number. Lines 17-24 run in both cases. Then 27 - 35 only in part 2.
# Once we have the big number, jumps back down to 1 where the factoring code lives.
17 addi 5 2 5       # f = f + 2
18 mulr 5 5 5       # f = f * f
19 mulr 4 5 5       # f = 19 * f
20 muli 5 11 5      # f = f * 11
21 addi 2 1 2       # c = c + 1
22 mulr 2 4 2       # c = 22 * c
23 addi 2 6 2       # c = c + 6
24 addr 5 2 5       # f = c + f
25 addr 4 0 4       # jmp (26 + a) [i.e. 27 when you start with a==1 (part 2)]
26 seti 0 0 4       # jmp 1
27 setr 4 5 2       # c = 27
28 mulr 2 4 2       # c = c * 28
29 addr 4 2 2       # c = c + 29
30 mulr 4 2 2       # c = c * 30
31 muli 2 14 2      # c = c * 14
32 mulr 2 4 2       # c = c * 32
33 addr 5 2 5       # f = f + c
34 seti 0 5 0       # a = 0
35 seti 0 2 4       # jmp 1
```

## Equivalent python code
```python3
c,f = 0,0
f = f + 2
f = f * f
f = 19 * f
f = f * 11
c = c + 1
c = 22 * c
c = c + 6
f = c + f
print("part 1 number", f)
p1n = f
c = 27
c = c * 28
c = c + 29
c = c * 30
c = c * 14
c = c * 32
f = f + c
print("part 2 number", f)
p2n = f

assert(p2n == 10551264)

def find_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    return sorted(divisors)

print(sum(find_divisors(p1n)))
print(sum(find_divisors(p2n)))
```

## State during big num computation in pt 2
```
# 0 [1, 0, 0, 0, 0, 0]
# 17 [1, 0, 0, 0, 17, 0]
# 18 [1, 0, 0, 0, 18, 2]
# 19 [1, 0, 0, 0, 19, 4]
# 20 [1, 0, 0, 0, 20, 76]
# 21 [1, 0, 0, 0, 21, 836]
# 22 [1, 0, 1, 0, 22, 836]
# 23 [1, 0, 22, 0, 23, 836]
# 24 [1, 0, 28, 0, 24, 836]
# 25 [1, 0, 28, 0, 25, 864]
# 27 [1, 0, 28, 0, 27, 864]
# 28 [1, 0, 27, 0, 28, 864]
# 29 [1, 0, 756, 0, 29, 864]
# 30 [1, 0, 785, 0, 30, 864]
# 31 [1, 0, 23550, 0, 31, 864]
# 32 [1, 0, 329700, 0, 32, 864]
# 33 [1, 0, 10550400, 0, 33, 864]
# 34 [1, 0, 10550400, 0, 34, 10551264]
# 35 [0, 0, 10550400, 0, 35, 10551264]
```