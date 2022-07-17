import enum


def largestRectangleArea4( heights) -> int:
        maxArea = 0
        stack = [] # pair: (index, height)
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea      
def largestRectangleArea( heights):
    hstack,pstack=[],[]
    max_area=0 
    for i,h in enumerate(heights):
        start = i
        while(hstack and h<hstack[-1] ):
            height= hstack.pop()
            start = pstack.pop()
            area = (i-start)*height
            max_area = max(max_area,area)            
        hstack.append(h)
        pstack.append(start)
    i =len(heights)   
    while(hstack):
            start = pstack.pop()
            height = hstack.pop()
            area = (i-start)*height
            max_area = max(max_area,area)
    return max_area  

if __name__ == '__main__':
    heights = [2,1,4,5,3,6]
    print(largestRectangleArea(heights))        
            
        

