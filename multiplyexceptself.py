from operator import __mul__
n = int(raw_input())
l = []
for _ in range(n):
    l.append(int(raw_input()))

n_zero = len(filter(lambda x:x == 0, l))
if n_zero == n:
    all_product = 0
else:
    all_product = reduce(__mul__, filter(None, l))
if n_zero >= 2:
    for _ in range(n):
        print 0
elif n_zero == 1:
    for ele in l:
        if ele != 0:
            print 0
        else:
            print all_product
elif n_zero == 0:
    for ele in l:
        print all_product / ele
