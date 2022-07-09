def sieve_of_eratosthenes_modified(n):
    """
    Sieve of Eratosthenes implementation
    with a tweak:
        Instead of true-false calculate the number
        of prime numbers to generate the composites.
    """
    primes = [0] * (n + 1)
    primes[0] = -1
    primes[1] = -1
    for i in range(2, n + 1):
        if not primes[i]: # 0 for prime
            for j in range(i + i, n + 1, i):
                primes[j] += 1
    return [i for i in range(2, n + 1) if primes[i] >= 3]



def lucky_number(n):
    NB= 3000
    numbers = [0]*NB
    lucky = [False]*NB
    found_lucky=0
    for i in range(2,NB):
        if(numbers[i]==0):
            for j in range(2*i,NB,i):
                numbers[j]= numbers[j]+1
                #print(j,numbers[j],i)
                if(numbers[j]==3):
                    lucky[j]=True
                    found_lucky=found_lucky+1
                    # if(found_lucky==n):
                    #     return (j,i)
                    # else: 
                    #     break  
    k=0
    for idx, x in enumerate(lucky) :
        if(x==True):
            k=k+1
        if(k==n):
            return idx    

    return (lucky[n]  )                    
                        

if __name__ == "__main__":
    res = sieve_of_eratosthenes_modified(2700)
    T = int(input())
    for t in range(T):
        n = int(input())
        print(res[n-1])
    # t = int (input())
    # for i in range(t):
    #     n = int(input())
    #     print(lucky_number(n))