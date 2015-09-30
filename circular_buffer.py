N = int(raw_input())

class Node:
    earliest = None
    current = None
    size = 0
    def __init__(self, s):
        self.s = s

def add(s):
    if Node.current is None:
        Node.current = Node.earliest = Node(s)
        Node.current.prev = Node.current.next = Node.current
        Node.size = 1
    elif Node.size < N:
        tmp = Node.current.next
        new = Node(s)
        Node.current.next = new
        new.next = tmp
        new.prev = Node.current
        tmp.prev = new
        Node.size += 1
        Node.current = new
    elif Node.size == N:
        if N > 1:
            Node.earliest = Node.earliest.next
            Node.current = Node.current.next
            Node.current.s = s
        elif N == 1:
            Node.current.s = s
def remove(nremove):
    for _ in range(nremove):
        if Node.size == 1:
            Node.current = Node.earliest = None
            Node.size = 0
        else:
            r = Node.earliest
            p = r.prev
            n = r.next
            p.next = n
            n.prev = p
            Node.earliest = n
            Node.size -= 1

def list_buffer():
    n = Node.earliest
    while True:
        print n.s
        if n == Node.current: break
        n = n.next

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

