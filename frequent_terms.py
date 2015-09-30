import heapq
from collections import Counter
n = int(raw_input())
l = []
for i in range(n):
    l.append(raw_input())
c = Counter(l)
for k in c:
    c[k] = -c[k]

n = int(raw_input())
l = [(x[1], x[0]) for x in c.items()]
heapq.heapify(l)
for _ in range(n):
    print heapq.heappop(l)[1]
