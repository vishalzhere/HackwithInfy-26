def charge(n,m,h,a,b):
    total = 0
    a.sort(reverse=True)
    b.sort(reverse = True)
    
    itera = min(m,n)
    for i in range(itera):
        fuel = b[i]*h
        
        total+=min(a[i],fuel)

    return total 
        
   


n , m ,h = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))


print(charge(n,m,h,a,b))