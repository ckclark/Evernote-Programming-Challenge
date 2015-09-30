INT_MIN = -2147383648
TOP_N = 4
top_four = [INT_MIN] * TOP_N
n = int(raw_input())
for _ in xrange(n):
    num = int(raw_input())
    for i, d in enumerate(top_four):
        if d < num:
            for x in xrange(TOP_N - 1, i, -1):
                top_four[x] = top_four[x - 1]
            top_four[i] = num
            break

print '\n'.join(map(str, top_four[:n]))
