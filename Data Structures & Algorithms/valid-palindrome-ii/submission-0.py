class Solution:
    def validPalindrome(self, s: str) -> bool:
        # when removing ch, we need to try remove the left ch or the right one->O(n)
        # check palindrom: reverse string + compare
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l+1:r+1], s[l:r]
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            l, r = l + 1, r -1
        
        return True

