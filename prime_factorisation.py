def smallest_factor(n):
    primes = [True]*(n+1)
    smallest_factor = [1]*(n+1)
    for i in range(2,n+1):
        if(primes[i]):
            for j in range(2*i,n+1,i):
                if(smallest_factor[j]==1): smallest_factor[j]=i
                primes[j]=False
    return(smallest_factor)
def factor(n,smallest_factors):
    if(smallest_factors[n]==1):
        res = str(n) 
        return res
    s= smallest_factors[n]
    n= int(n/s)
    res=  str(s) + ' x ' + factor(n,smallest_factors)
    return res
    
def factorize(n):
    sm = smallest_factor(n)
    res =factor(n,sm)
    print('1 x '+res)

if __name__ == "__main__":
    while True:
        try:
            n = input()
            if n:
                n = int(n)
                factorize(n)
            else:
                break
        except EOFError:
            break
    

    