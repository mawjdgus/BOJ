#알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
#1. 길이가 짧은 것부터
#2. 길이가 같으면 사전 순으로
import sys
T = int(sys.stdin.readline())
dictionary = []
for _ in range(T):
    dictionary.append(str(sys.stdin.readline().strip()))
dictionary = set(dictionary)
dictionary = list(dictionary)
dictionary.sort()
dictionary.sort(key = len)

for a in dictionary:
    print(a)


#####
# import sys
# word=set()
# for i in range(int(input())):
#     word.add(sys.stdin.readline().rstrip())
# word=list(word)
# word.sort()
# word.sort(key=lambda x:len(x))
# print("\n".join(word))

