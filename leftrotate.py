n,d=map(int,input().split())
arr=list(map(int,input().split()))[:n]
for i in range(0,d):
    temp=arr[0]
    for j in range(0,n-1):
        arr[j]=arr[j+1]
    arr[n-1]=temp
for i in range(0,n):
    print(arr[i],end=" ") 

