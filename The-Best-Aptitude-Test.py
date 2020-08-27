# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
 
def correlation(sx, sy):
    n = len(sx)
    x, y, xy, xsq, ysq = 0, 0, 0, 0, 0
    for xi, yi in zip(sx, sy):
        x += xi
        y += yi
        xy += xi*yi
        xsq += xi*xi
        ysq += yi*yi
    sq = math.sqrt((n*xsq - x*x)*(n*ysq - y*y))
    if sq:
        return (n*xy - x*y) / sq
    return 0
 
for t in range(int(input())):
    input()
    gpa = list(map(float, input().split()))
    max_r = -2
    max_i = 0
    for i in range(1,6):
        apt_test = list(map(float, input().split()))
        r = correlation(gpa, apt_test)
        if r > max_r:
            max_r = r
            max_i = i
    print(max_i)