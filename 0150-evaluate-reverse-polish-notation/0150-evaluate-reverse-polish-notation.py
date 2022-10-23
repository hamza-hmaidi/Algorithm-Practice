class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if(x not in ['+','-','*','/']):
                c=int(x)
                stack.append(c)
            else:
                c1= stack.pop()
                c2= stack.pop()
                if(x =='+'):
                    res = c1+c2
                elif(x=='-'):
                    res = c2-c1
                elif(x=='*'):
                    res=c1*c2
                elif(x=='/'):
                    res=int( c2 / c1)
                stack.append(res)
        return stack.pop()
                
        