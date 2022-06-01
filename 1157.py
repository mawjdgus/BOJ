import sys

in_ = list(sys.stdin.readline().strip().upper())
in_set = set(in_)

result = []
for a in in_set:
    result.append(in_.count(a))


if result.count(max(result)) >= 2:
    print("?")
else:
    in_set = list(in_set)
    print(in_set[result.index(max(result))])
    
    
# ===========================
# n = input()
# n = n.upper()
# alpa='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# result = []
# for i in alpa:
#   result.append(n.count(i))
# if result.count(max(result)) > 1:
#   print("?")
# else:
#   print(alpa[result.index(max(result))])