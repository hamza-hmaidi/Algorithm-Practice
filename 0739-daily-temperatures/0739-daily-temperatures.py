class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res=[0]*len(temps)
        stack=[]
        for i in range(len(temps)):
            while( len(stack)>0 and temps[i]>stack[-1][0]):
                t= stack.pop()
                res[t[1]]=i-t[1]
            stack.append((temps[i],i)) 
        return res    