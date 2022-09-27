
class Solution:
    t =[0]*46
    def climbStairs(self, n: int) -> int:
        if(n==2):
            return 2
        elif (n==1):
            return 1    
        if (not self.t[n-1]):
            self.t[n-1]=self.climbStairs(n-1) 
        if (not self.t[n-2]):    
            self.t[n-2]=self.climbStairs(n-2)
        self.t[n]= self.t[n-1]+self.t[n-2]
        return self.t[n]
if __name__ == '__main__':
    sol =  Solution()
    print(sol.climbStairs(4))