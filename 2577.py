
import sys

mul = 1
for test_case in range(0, 3):
    num = int(sys.stdin.readline())
    mul *= num
    
result = [0 for i in range(0, 10)]
for a_num in str(mul):
    for i in range(0, 10):
        if str(i) == a_num:
            result[i] += 1
            break
        else:
            continue
        

for a in result:
    print(a)
            