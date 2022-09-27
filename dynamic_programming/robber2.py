def rob(nums):
    rob1,rob2=0,0
    for i in range(len(nums)-1):
        temp = max(rob1+nums[i],rob2)
        rob1=rob2
        rob2=temp 

    rob1,rob2=0,0
    for i in range(1,len(nums)):
        temp1 = max(rob1+nums[i],rob2)
        rob1=rob2
        rob2=temp1
    return max(temp1,temp)   
if __name__ == '__main__':
    nums= [1,2,3,1]
    print(rob(nums))


