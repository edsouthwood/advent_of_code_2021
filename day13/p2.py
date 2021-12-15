points = []
lines = []
with open("data.txt") as f:
    toggle = True
    for line in f:
        if line == '\n':
            toggle = False
        if toggle:
            points += [line.strip('\n')]
        else:
            if line == '\n':
                pass
            else:
                lines += [line.strip('\n')]
class point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def reflect(self, line):
        line = line.split("=")
        if line[0] == 'x':
            if self.x < int(line[1]):
                return
            else:
                self.x = 2*int(line[1]) - self.x
                return
        else:
            if self.y < int(line[1]):
                return
            else:
                self.y = 2*int(line[1]) - self.y
                return
    
    def to_tup(self):
        return tuple([self.x,self.y])

pnts = []
for p in points:
    p = p.split(',')
    pnts += [point(int(p[0]),int(p[1]))]

lns = []
for l in lines:
    l = l.lstrip("fold along ")
    lns += [l]

for l in lns:
    for p in pnts:
        #print(p.x,p.y,"reflected in line",l)
        p.reflect(l)
        #print(p.x,p.y)

x_max = 0
y_max = 0
for p in pnts:
    if p.x > x_max:
        x_max = p.x
    if p.y > y_max:
        y_max = p.y
#print(x_max,y_max)

import numpy as np
grid = np.zeros([y_max+1,x_max+1])
for p in pnts:
    grid[p.y][p.x] += 1
print(grid)
