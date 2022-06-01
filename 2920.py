import sys

major = list(map(int,sys.stdin.readline().strip().split()))
result = 'mixed'
for i, a in enumerate(major):
    if i == 0 and major[i+1] < a:
        result='descending'
        continue
    if i == 0 and major[i+1] > a:
        result='ascending'
        continue
    
    if result=='descending' and major[i-1] < a:
        result='mixed'
        break
    if result=='ascending' and major[i-1] > a:
        result='mixed'
        break
    
print(result)
        
#####################
# print({"2345678":"ascending","7654321":"descending"}.get(input()[2::2],"mixed"))