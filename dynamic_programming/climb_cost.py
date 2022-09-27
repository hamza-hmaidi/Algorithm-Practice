
class Solution:
    t = [-1]*1000 

    @staticmethod 
    def climb(cost,start,tot,t):
        if(start>=len(cost)-2):
            return tot
        if(t[start+2]==-1):
            t[start+2]=cost[start+2]+ Solution.climb(cost,start+2,tot,t)    
        if(t[start+1]==-1):
            t[start+1]=cost[start+1]+ Solution.climb(cost,start+1,tot,t)
        tot+= t[start+1] if(t[start+1]<t[start+2]) else t[start+2]
        return tot
    def minCostClimbingStairs(self, cost) -> int:
        tot,start =0,-1
        t = [-1]*1000 
        return Solution.climb(cost,start,tot,t)
   
if __name__ == '__main__':
    cost = [1,100,1,1,1,100,1,1,100,1]
    sol = Solution()
    print(sol.minCostClimbingStairs(cost))