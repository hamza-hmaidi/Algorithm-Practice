class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r =0,len(nums)-1
        m = int((l+r)/2)
        while(l<r and nums[m] != target ):
            if(nums[m]>target):
                r=m-1
            elif(nums[m]<target):
                l=m+1
            m = int((l+r)/2)
        return m if( nums[m]==target) else -1     
   
        