import sys


T = int(sys.stdin.readline())

for test_case in range(1,T+1):
    in_ = list(map(str,sys.stdin.readline().strip().split(' ')))
    re = int(in_[0])
    st = in_[1]
    
    for alpha in st:
        for _ in range(0,re):
            print(alpha, end='')
    print('')