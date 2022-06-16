class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for c in s:
            if c in ["(","{","["]:
                stack.append(c)
            else:
                if not stack:
                    return False
                char=stack.pop()
                if char=='(' and c!=')':
                    return False
                if char=='{' and c!='}':
                    return False
                if char=='[' and c!=']':
                    return False
        if stack:
            return False
        return True