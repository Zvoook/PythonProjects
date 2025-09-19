h = [1, 8, 6, 2, 5, 4, 8, 3, 7]
p1=0, p2=len(h)-1

def area(h1, h2, p1, p2):
    return (min(h1,h2))*(p2-p1)

max_area=area(h[p1], h[p2], p1, p2)

while p2!=p1:
    cur=area(h[p1], h[p2], p1, p2)
    if cur>max_area: max_area = cur
    if h[p1]>h[p2]: p1+=1
    else: p2-=1
print('The max area is ', max_area)