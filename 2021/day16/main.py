from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def bitstream(packet):
    for ch in packet:
        dig = int(ch, 16)
        yield((dig >> 3) & 1)
        yield((dig >> 2) & 1)
        yield((dig >> 1) & 1)
        yield((dig) & 1)

def nbit(n, bitstream):
    acc = 0
    for _ in range(n):
        acc = acc << 1 | next(bitstream)
    return acc

def product(*args):
    acc = 1
    for a in args:
        acc *= a
    return acc
def mmin(*args): return min(args)
def mmax(*args): return max(args)
def msum(*args): return sum(args)
def gt(a,b): return 1 if a > b else 0
def lt(a,b): return 1 if a < b else 0
def eq(a,b): return 1 if a == b else 0

TYPE_ID_TO_OPERATOR = {0: "msum", 1: "product", 2: "mmin", 3: "mmax", 4: "", 5: "gt", 6: "lt", 7: "eq"}

def parse(bitstream, max_p=math.inf):
    parsed = 0
    try:
        while parsed < max_p:
            version = nbit(3, bitstream)
            yield "version", version
            type_id = nbit(3, bitstream)
            parsed += 1
            if type_id == 4:
                more = nbit(1, bitstream)
                acc = nbit(4, bitstream)
                while more:
                    acc = acc << 4
                    more = nbit(1, bitstream)
                    acc |= nbit(4, bitstream)
                yield str(acc) + ","
            else:
                yield TYPE_ID_TO_OPERATOR[type_id]
                len_type = nbit(1, bitstream)
                yield "("
                if len_type == 0:
                    total_len = nbit(15, bitstream)
                    for tok in parse(itertools.islice(bitstream, total_len)):
                        yield tok
                else:
                    num_sub_packets = nbit(11, bitstream)
                    for tok in parse(bitstream, max_p=num_sub_packets):
                        yield tok
                yield "),"
    except StopIteration:
        pass
    

def part1():
    packet = bitstream(input[0])
    return sum([x[1] for x in parse(packet) if x[0] == "version"])

def part2():
    expression = "".join([x for x in parse(bitstream(input[0])) if type(x) == str]).replace(",)", ")")[:-1]
    return(eval(expression))

print(part1())
print(part2())