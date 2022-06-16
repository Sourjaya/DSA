class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        sign=1
        output,cur=0,0
        for c in s:
            if c.isdigit():
                cur=cur*10+int(c)
            elif c in "+-":
                output+=(cur*sign)
                cur=0
                if c=="-":
                    sign=-1
                else:
                    sign=1
            elif c=="(":
                stack.append(output)
                stack.append(sign)
                output=0
                sign=1
            elif c==")":
                output+=(cur*sign)
                output*=stack.pop()
                output+=stack.pop()
                cur=0
        return output+(cur*sign)