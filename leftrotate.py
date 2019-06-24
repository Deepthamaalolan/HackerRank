def leftRotate(arr, d, n): 
    g_c_d = gcd(d, n) 
    for i in range(g_c_d):   
        temp = arr[i] 
        j = i 
        while 1: 
            k = j + d 
            if k >= n: 
                k = k - n 
            if k == i: 
                break
            arr[j] = arr[k] 
            j = k 
        arr[j] = temp 
  
 
def printArray(arr, size): 
    for i in range(size): 
        print (arr[i],end =" ") 

def gcd(a, b): 
    if b == 0: 
        return a; 
    else: 
        return gcd(b, a % b) 
n,d=map(int,input().split()) 
arr =list(map(int,input().split()))[:n]
leftRotate(arr, d, n) 
printArray(arr, n) 
