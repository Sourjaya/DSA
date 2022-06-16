class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=0
        for i in range(len(accounts)):
            total=sum(accounts[i])
            m=max(m,total)
        return m
