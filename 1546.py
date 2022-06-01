from statistics import mean
import sys
import math

exam = int(sys.stdin.readline())

exam_list = list(map(int,sys.stdin.readline().split(' ')))
new_score = []
for score in exam_list:
    new_score.append(score/max(exam_list)*100)
    
print(mean(new_score))

# #### 

# max=0
# n=int(input())
# sum=0
# sub=list(map(int,input().split()))
# for i in range(0,n):
#     if sub[i]>max:
#         max=sub[i]
#     sum+=sub[i]
# for i in range(0,n):
#     print(sum*100/max/n)

