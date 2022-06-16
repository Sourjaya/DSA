class Solution:
    def intToRoman(self, num: int) -> str:
        sym = [["I",1],["IV",4],["V",5],["IX",9],["X",10],["XL",40],["L",50],["XC",90],["C",100],["CD",400],["D",500],["CM",900],["M",1000]]
        res =""
        for s, val in reversed (sym):
            if num // val:
                c = num // val
                res += (s* c)
                num = num % val
        return res

        