class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curres = []
        n = len(s)

        def backtrack(j,i):
            if i >= n:
                if i == j:
                    res.append(curres[::])
                return
            
            if isPalindrome(j, i):
                curres.append(s[j:i+1])
                backtrack(i+1, i+1)
                curres.pop()
            backtrack(j, i+1)
                
        def isPalindrome(i,j):
            while i<j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True
        backtrack(0,0)
        return res