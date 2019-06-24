n=int(input())
l=[]
s=[]
for i in range(0,n):
    arr=input()
    l.append(arr)
q=int(input())
for i in range(0,q):
    query=input()
    s.append(query)
for i in s:
    count=0
    for j in l:
        if i==j:
            count=count+1
    print(count)
