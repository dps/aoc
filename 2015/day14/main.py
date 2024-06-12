
from utils import *

D = [i.strip() for i in open("input","r").readlines()]


time = 2503

deer = []
points = defaultdict(int)

p1_winner = 0

for line in D:
    v,t,r = ints(line)
    name = line.split()[0]
    dist, run_left, rest_left = 0, t,0
    deer.append((dist, name, v,t,r, run_left, rest_left))
    segment = t+r
    dist = ((v*t) * (time//segment)) + min(time%(segment), t)*v
    p1_winner = max(dist, p1_winner)

print(p1_winner)

for elapsed, _ in enumerate(range(time)):
    new_deer = []
    for dist, name, v,t,r, run_left, rest_left in deer:
        if run_left > 0:
            dist += v
            run_left -= 1
            if run_left == 0:
                rest_left = r
        elif rest_left > 0:
            rest_left -= 1
            if rest_left == 0:
                run_left = t

        new_deer.append((dist,name, v,t,r, run_left, rest_left ))

    dd = sorted(new_deer, reverse=True)
    winning_d = dd[0][0]
    for i,doe in enumerate(dd):
        if doe[0] >= winning_d:
            points[doe[1]] += 1
        else:
            break
    
    deer = new_deer

print(max(points.values()))
        
