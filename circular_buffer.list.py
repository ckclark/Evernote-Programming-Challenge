N = int(raw_input())
buffer = [None] * N
head = None
tail = None
size = 0

def add(s):
    global head, tail, size
    if head is None:
        head, tail = 0, 0
        buffer[head] = s
        size = 1
    elif size < N:
        head = (head + 1) % N
        buffer[head] = s
        size += 1
    elif size == N:
        head = (head + 1) % N
        tail = (tail + 1) % N
        buffer[head] = s

def remove(nremove):
    global head, tail, size
    tail = (tail + nremove) % N
    size -= nremove
    if size == 0:
        head, tail = None, None

def list_buffer():
    global head, tail
    c = tail
    while True:
        print buffer[c]
        if c == head:
            break
        c = (c + 1) % N

while True:
    line = raw_input()
    if line[0] == 'Q': break
    elif line[0] == 'A':
        nline = int(line.split()[-1])
        for i in range(nline):
            add(raw_input())
    elif line[0] == 'R':
        nremove = int(line.split()[-1])
        remove(nremove)
    elif line[0] == 'L':
        list_buffer()

