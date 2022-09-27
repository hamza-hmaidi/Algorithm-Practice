def maxProfit( prices):
    sell,buy,profit=0,prices[0],0
    for p in prices[1:]:
        if(p<buy):
            buy=p
        elif (p>buy ):
            newprofit = p - buy
            if(newprofit>profit):
                profit= newprofit
                sell=p
    return profit

if __name__ == '__main__':
    prices = [1,0]
    print(maxProfit(prices))            

