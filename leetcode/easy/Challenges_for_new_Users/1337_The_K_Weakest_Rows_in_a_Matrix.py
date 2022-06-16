class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res=[]
        for index,ind in enumerate(mat):
            row=(sum(ind),index)
            res.append(row)
        res.sort()
        return [i[1] for i in res[:k]]
