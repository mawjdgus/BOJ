
# 소수 찾기

import sys

input = sys.stdin.readline

def sol1978():
    N = int(input())
    nums = list(map(int,input().strip().split(' ')))
    sosu = 0
    for num in nums: # 숫자들을 불러온다.
        error = 0
        if num > 1: # 일단 1보다 커야되고
            for i in range(2, num): # 2부터 제곱근 - 1 까지 숫자에서 직접 나눠본 뒤
                if num % i == 0: # 만약 나눠지는게 있으면 안됨
                    error += 1
            if error == 0:
                sosu += 1
        else:
            continue
    return sosu

if __name__ == "__main__":
    print(sol1978())
    
    
    
    
    
    
    
    
    
##############

n=int(input())
li=list(map(int,input().split()))
cnt=0
for i in li:
    f=True
    if i<=1:continue
    for j in range(2,i):
        if i%j==0:
            f=False
            break
    if f:
        cnt+=1
print(cnt)
    