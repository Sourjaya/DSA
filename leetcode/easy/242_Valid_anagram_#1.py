class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Solution 3- Space efficient [O(1),if sorting takes O(1) space] but time complexity becomes[O(nlogn)].
        '''
        return sorted(s)==sorted(t)
        '''
        #Solution 2-The above line of code does the operations automatically in python.Counter is a hashmap that counts automatically.
        '''
        return Counter(s)==Counter(t)
        '''
        #Solution 3
        if len(s)!= len(t):
            return False
        countS,countT={},{}
        for i in range(len(s)):
            countS[s[i]]=1+countS.get(s[i],0)
            countT[t[i]]=1+countT.get(t[i],0)
        for c in countS:
            if countS[c]!=countT.get(c,0):
                return False
        return True
