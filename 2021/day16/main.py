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

def product(*args): return reduce(operator.mul, args, 1)
def _min(*args): return min(args)
def _max(*args): return max(args)
def _sum(*args): return sum(args)
def gt(a,b): return 1 if a > b else 0
def lt(a,b): return 1 if a < b else 0
def eq(a,b): return 1 if a == b else 0

TYPE_ID_TO_OPERATOR = {0: "_sum", 1: "product", 2: "_min", 3: "_max", 4: "", 5: "gt", 6: "lt", 7: "eq"}

ver = 0

def parse(bitstream, max_p=math.inf):
    global ver
    parsed = 0
    try:
        while parsed < max_p:
            version = nbit(3, bitstream)
            ver += version
            type_id = nbit(3, bitstream)
            parsed += 1
            if type_id == 4:
                more = nbit(1, bitstream)
                acc = nbit(4, bitstream)
                while more:
                    more = nbit(1, bitstream)
                    acc = (acc << 4) | nbit(4, bitstream)
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

def solve():
    expression = "".join([x for x in parse(bitstream(input[0]))]).replace(",)", ")")[:-1]
    return(ver, eval(expression))

print(solve())