class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        out1,out2=[],[]
        for i in s:
            if i=='#':
                if out1:
                    out1.pop()
            else:
                out1.append(i)
        for i in t:
            if i=='#':
                if out2:
                    out2.pop()
            else:
                out2.append(i)
        if out1==out2:
            return True
        else:
            return False
