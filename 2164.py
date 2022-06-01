from collections import deque
import sys

N = int(sys.stdin.readline())
a = []
for i in range(1,N+1):
    a.append(i)

queue = deque(a)
while True:
    if len(queue) == 1:
        print(queue.pop())
        break
    queue.popleft()
    queue.rotate(-1)
