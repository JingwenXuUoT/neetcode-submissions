class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ignore all non-alphanumeric characters
        s_cleaned = ("".join(filter(str.isalnum, s))).lower()
        
        left = 0
        right = len(s_cleaned)-1

        while(left<right):
            if(s_cleaned[left] != s_cleaned[right]):
                return False
            left+=1
            right-=1
        
        return True
