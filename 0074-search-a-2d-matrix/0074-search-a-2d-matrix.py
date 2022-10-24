class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bot=0,len(matrix)-1
        while(top<=bot):
            m= (top+bot)//2
            if(matrix[m][0]>target):
                bot=m-1
            elif(matrix[m][-1]<target):
                top=m+1
            else:
                break
        if(top> bot):
            return False
        print(m)    
        l,r=0,len(matrix[m])-1
        while(l<=r):
            m2= l+ (r-l)//2
            if(matrix[m][m2]>target):
                r=m2-1
            elif(matrix[m][m2]<target):
                l=m2+1
            else:
                return True
            
        return False     
                