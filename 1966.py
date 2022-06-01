## 풀다 울화 터질뻔
import sys
from collections import deque

T = int(input()) # 입력 받는다
# rotate -> num 만큼 회전한다. 양수면 오른쪽, 음수면 왼쪽.
for _ in range(T):
    N, M = map(int,input().split()) # N -> 몇개 받을지, M -> 몇번째 있는 애를 뽑을지.
    queue = deque(list(map(int,input().split()))) # queue로 만든다.
    Z = queue[M] # 내가 원하는 값을 저장해놓는다.
    cnt = 0 # 몇번째로 뽑히는지 print(cnt)하기 위한 cnt 값 초기는 당연히 0이다.
    while True: # 내가 원하는 놈이 queue[M] -> Z 가 출력될때까지 계속 돈다
        if max(queue) == queue[0]: # 만약에 queue의 최대값이 제일 왼쪽 queue값과 같을때만 pop을 해준다.
            pop = queue.popleft() # left pop 
            cnt += 1 # 그리고 cnt하나 올려준다
            # 원래 인덱스
            # queue[M]이 몇번째로 나오는지 찾는건데 이 때 index 는 M
            if M == 0: # 이때 만약에, M이 0이라면, 0번째 있는 값이 이미 나왔으므로  # 만약 M이 0 이 아니라면 else로 넘어간다
                if Z == pop: # pop과 내가 원래 원하는 값이 맞으면
                    print(cnt) # cnt = 0 을 출력해준다
                    break
                M += N-cnt-1 # 
            else:
                M -= 1 # 내가 원하는 놈은 하나 준 숫자의 인덱스로 오게된다. 즉 2번째 인덱스였다면 1번째 인덱스로
            
        else:
            queue.rotate(-1) # 그리고 만약에 queue최대값이 제일 왼쪽queue값과 다르면, rotate로 오른쪽으로 보내준다
            if M != 0 : # 이때 만약 M이 0이 아니라면
                M -= 1 # M은 한칸 왼쪽으로
            else: # 만약에 0이 맞다면
                M += N-cnt-1 # 가장 마지막으로 간다.