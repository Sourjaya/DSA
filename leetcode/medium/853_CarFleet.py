class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Approach using pair->position:speed and stack
        '''
        stack=[]
        #pair=[[p,s] for p,s in zip(position,speed)]
        pair = zip(position,speed)
        for p,s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        '''
        #Approach using pair->position:((target-position)/speed) without stack
        count=1
        pair=[[p,((target-p)/s)] for p,s in zip(position,speed)]
        tt=0
        flag=0
        for p,t in sorted(pair)[len(pair)-1::-1]:
            if flag==0:
                tt=t
                flag=1
            if t>tt:
                count+=1
                tt=t
        return count
