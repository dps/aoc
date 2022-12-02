scores = {'X':1,'Y':2,'Z':3}
outcome = {'AX': 3, 'AY': 6, 'AZ': 0, 'BX': 0, 'BY': 3, 'BZ': 6, 'CX': 6, 'CY': 0, 'CZ': 3}
def first():
    inp = open('input.txt', 'r')
    lines = inp.readlines()

    score = 0
    for line in lines:
        m = line.strip().split(" ")
        theirs = m[0]
        mine = m[1]
        score = score + scores[mine] + outcome[theirs+mine]
    print(score) 


def second():
    inp = open('input.txt', 'r')
    lines = inp.readlines()

    score = 0
    for line in lines:
        m = line.strip().split(" ")
        theirs = m[0]
        dot = m[1]
        if dot == 'X': # lose
            if theirs == 'A':
                mine = 'Z'
            if theirs == 'B':
                mine = 'X'
            if theirs == 'C':
                mine = 'Y'
        if dot == 'Y': # draw
            if theirs == 'A':
                mine = 'X'
            if theirs == 'B':
                mine = 'Y'
            if theirs == 'C':
                mine = 'Z'
        if dot == 'Z': # win
            if theirs == 'A':
                mine = 'Y'
            if theirs == 'B':
                mine = 'Z'
            if theirs == 'C':
                mine = 'X'
        
        score = score + scores[mine] + outcome[theirs+mine]
    print(score) 


if __name__ == '__main__':
    second()


