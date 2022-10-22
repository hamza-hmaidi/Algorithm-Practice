class Solution:
    def equalDic(self,dict1,dict2) -> bool:
        if len(dict1)!=len(dict2):
            return False
     
        else:

            flag=0
            for i in dict1:
                if dict1.get(i)!=dict2.get(i):
                    flag=1
                    break
            if flag==0:
                return True
            else:
                return False
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1)>len(s2)):
            return False
        count1={}
        count2={}
        l=0
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        for i in range(len(s1)):
            count2[s2[i]] = 1+ count2.get(s2[i],0)
            
        if(self.equalDic(count1,count2)):
            return True
        
        for r in range(len(s1),len(s2)):
            
            count2[s2[r]]= 1+ count2.get(s2[r],0)
            count2[s2[l]]=count2.get(s2[l],0)-1
            if( count2[s2[l]]==0):
                count2.pop(s2[l])
            if(self.equalDic(count1,count2)):
                return True    
            l+=1
        return False        
                
        
        