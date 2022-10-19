class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs :
            s2 = "".join(sorted(s))
            if(s2 in dic):
                dic[s2].append(s)
            else:
                dic[s2]=[s]
        return dic.values()       
                
            