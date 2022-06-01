import sys

result = list(map(str,sys.stdin.readline().strip().split(' ')))

if '' in result:
    print(0)
else:
    print(len(result))
    
#=============================
# import sys
# s = sys.stdin.read().strip()
# if not s:
#     print("0")
# else:
#     print(len(s.split(" ")))