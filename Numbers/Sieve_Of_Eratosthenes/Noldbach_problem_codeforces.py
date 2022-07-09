def Noldbach(n,k):
    numbers = [True]*(n+1)
    prev= 2
    sum =0
    count =0
    sums=[]
    for i in range(2,n):
        if(numbers[i]==True):
            if(i>2):
                sum = prev + i +1 
                if(sum>=2 and sum<=n ):
                    sums.append(sum)
                prev = i    
            for j in range(2*i,n,i):
                numbers[j]=False
    for sum in sums :
        if(numbers[sum]): 
            count+=1            
    return (count>=k)            

if __name__ == "__main__":
    inp = list(map(int, input().split()))
    #print(Noldbach(inp[0],inp[1]))
    print('YES') if Noldbach(inp[0],inp[1]) else print('NO')