
import sys


while True:
    in_ = list(str(sys.stdin.readline().strip()))
    if ''.join(in_) == '0':
        break
    in_re = in_[::-1]
    c = 1
    for i in range(len(in_)):
        if in_[i] != in_re[i]:
            c=0
            break
        else:
            continue
    if c == 0:
        print('no')
    else:
        print('yes')
    

    