input = [i.strip() for i in open("input.txt","r").readlines()]

# Merry Christmas!
#        * 
#       /'\
#      /^.;\
#      /:` \
#     /:.`' \ 
#       | |

DMAP = {'0': 0, '1': 1, '2':2, '=':-2, '-': -1}
SMAP = {0:'0',1:'1',2:'2',3:'=',4:'-'}
def snafu_to_dec(snafu):
    exp = len(snafu) - 1
    acc = 0
    for dig in snafu:
        acc += (pow(5, exp) * DMAP[dig])
        exp -= 1
    return acc

def dec_to_snafu(num):
    r = ""
    while num > 0:
        td = num % 5
        chr = SMAP[td]
        r = chr + r
        if chr in "-=":
            num += 5
        num //= 5
    return r

def solve():
    print(dec_to_snafu(sum(snafu_to_dec(x) for x in input)))

if __name__ == '__main__':
    solve()
