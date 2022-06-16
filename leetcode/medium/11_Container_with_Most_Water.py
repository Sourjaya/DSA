class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Brute Force Solution
        '''
        res=0
        for l in range(len(height)):
            for r in range(l+1,len(height)):
                a=(r-l)* min(height[l],height[r])
                res=max(res,a)
        return res
        '''
        res=0
        l,r=0,len(height)-1
        while l<r:
            a=(r-l)* min(height[l],height[r])
            res=max(res,a)
            if(height[l]<height[r]):
                l+=1
            else:
                r-=1
        return res