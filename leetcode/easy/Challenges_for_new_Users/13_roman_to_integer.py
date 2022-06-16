class Solution:
    def romanToInt(self, s: str) -> int:
        mapr={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        num=0
        for i in range(len(s)):
            if(i+1<len(s) and mapr[s[i]]<mapr[s[i+1]]):
                num=num-mapr[s[i]]
            else:
                num=num+mapr[s[i]]
        return num