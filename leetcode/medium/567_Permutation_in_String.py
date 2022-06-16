class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):return False
        s1Count,s2Count={},{}
        for i in range(26):
            s1Count[chr(97+i)]=0
            s2Count[chr(97+i)]=0
        for i in range(len(s1)):
            s1Count[s1[i]]=1+ s1Count.get(s1[i],0)
            s2Count[s2[i]]=1+ s2Count.get(s2[i],0)
        m=0 #matches
        for i in range(26):
            if s1Count[chr(97+i)]==s2Count[chr(97+i)]:
                m+=1
        l=0
        for r in range(len(s1),len(s2)):
            if m==26:
                return True
            s2Count[s2[r]]+=1
            if s1Count[s2[r]]==s2Count[s2[r]]:
                m+=1
            elif s1Count[s2[r]]+1==s2Count[s2[r]]:
                m-=1
            s2Count[s2[l]]-=1
            if s1Count[s2[l]]==s2Count[s2[l]]:
                m+=1
            elif s1Count[s2[l]]-1==s2Count[s2[l]]:
                m-=1
            l+=1
        return m==26
            