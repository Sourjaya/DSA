class Solution:
    """
        @param: strs: a list of strings
        @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res=""
        for s in strs:
            res+=str(len(s))+"@"+s
        return res

        """
        @param: str: A string
        @return: dcodes a single string to a list of strings
        """
    def decode(self, str):
        res,i=[],0
        j=i
        while i<len(str):
            if str[i] !="@":
                i+=1
            else:
                l=int(str[j:i])
                res.append(str[i+1:i+1+l])
                i=j=i+1+l
        return res