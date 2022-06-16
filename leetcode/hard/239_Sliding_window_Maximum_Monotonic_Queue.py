class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #Solution-1
        # indexQ = deque()
        # valQ = deque()
        
        # res = []
        # for i, n in enumerate(nums):
        #     while valQ and n > valQ[-1]:
        #         valQ.pop()
        #         indexQ.pop()
        #     valQ.append(n)
        #     indexQ.append(i)
            
        #     while i - indexQ[0] + 1 > k:
        #         valQ.popleft()
        #         indexQ.popleft()
        #     if i + 1 >= k:
        #         res.append(valQ[0])
        # return res

        #Solution-2
        output=[]
        q=collections.deque()
        l=r=0
        while r<len(nums):
            while q and nums[q[-1]]< nums[r]:
                q.pop()
            q.append(r)

            #remove left val from window
            if l>q[0]:
                q.popleft()
            if (r+1)>=k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output