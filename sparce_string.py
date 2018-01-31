import sys
N=int(input())
Q=int(input())

def accept_input(n):
    file1=[]
    for i in range(n):
        file1.append(raw_input())
    return file1

def match_string(str1,query):
    for i in range(len(query)):
        cnt=0
        for j in range(len(str1)):
            if str1[j]==query[i]:
                cnt+=1
        print(cnt)

str1=accept_input(N)
que=accept_input(Q)
match_string(str1,que)
