def rob(nums) -> int:
    if(len(nums)==1):
        return nums[0]
    s0,s1,i=nums[0],nums[1],0
    for n in nums[2:]:
        if(i%2==0):
            s1=max(s0,s1)
            s0+=n
        else:
            s0=max(s0,s1)
            s1+=n    
        i+=1
    return max(s1,s0)          
        
if __name__ == '__main__':
    nums= [1,3,1,3,100]
    print(rob(nums))

        
               