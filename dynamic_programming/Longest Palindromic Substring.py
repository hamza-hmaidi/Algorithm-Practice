# dict = {}
# class Solution:
#     def longestPalindrome(self,s): 
#         if(len(s)<=1):
#             dict[s]=s
#             return s
#         if(len(s)==2 and s[0]==s[1] ):
#             return s
#         if(s[0]==s[-1]):
#             insert(s[1:len(s)-1],dict)
#             if(dict[s[1:len(s)-1]]==s[1:len(s)-1]): 
#                 dict[s]=s[0]+dict[s[1:len(s)-1]]+s[0]
#             else:  
#                 dict[s]=dict[s[1:len(s)-1]] 
#             return dict[s]
#         s1= s[1:]
#         s2=s[:len(s)-1]
#         insert(s1,dict)
#         insert(s2,dict)    
#         if(s[0]==s[-1]):
#             dict[s]=s[0] + dict[s1] +s[0] 
#             return dict[s]
#         return dict[s1]  if len(dict[s1] )>len(dict[s2] ) else dict[s2] 

# def insert(s,dict):
#     sol = Solution()
#     if  dict.get(s) == None:
#         dict[s]=sol.longestPalindrome(s)
#     return dict[s]    
# if __name__ == '__main__':
#     sol = Solution()
#     print(sol.longestPalindrome('acabkaca'))
#     print(dict)
def longestPalindrome(s): 
    max=''
    for i in range(len(s)):
        l,r=i-1,i+1 
        while(l>=0 and r<len(s) and s[l]==s[r]):
            l-=1
            r+=1
        s1 = s[l+1:r]
        max = s1 if len(s1)> len(max) else max

        l,r=i,i+1
        while(l>=0 and r<len(s) and s[l]==s[r]):
            l-=1
            r+=1
        s2=s[l+1:r]
        max = s2 if len(s2)> len(max) else max     
    return max       
if __name__ == '__main__':
    print(longestPalindrome('a'))        

