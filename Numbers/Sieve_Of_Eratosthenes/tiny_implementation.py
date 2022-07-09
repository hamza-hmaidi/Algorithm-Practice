def printPrimes(start, end):
    primes = sieveOfErtosthenes(end)
    result = [i for i in primes if i>= start]
    return result

def sieveOfErtosthenes(end):
    primes = [True] * (end+1)
    result =[]
    for i in range(2,int(end ** 0.5)+1):
        if(primes[i]==True):
            result.append(i)
            for j in range(i*i, end,i):
                primes[j]=False
    # for i in range(int(end ** 0.5)+1,end):
    #     if(primes[i]==True):
    #         result.append(i)     

    return result + [i for i in range(int(end ** 0.5)+1,end) if primes[i] ]

if __name__ == "__main__":
    print (printPrimes(20,30))
