n, inputs = map(int,input().split())
list = [0]*(n+1)
for _ in range(inputs):
    x, y, incr =map(int,input().split())
    list[x-1] += incr
    if((y)<=len(list)): 
        list[y] -= incr;
max = x = 0
for i in list:
   x=x+i;
   if(max<x): 
       max=x;
print(max)
