class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Solution- One pass
        m={} #val:index
        for i,n in enumerate(nums):
            d=target-n
            if d in m:
                return [m[d],i]
            m[n]=i
        return