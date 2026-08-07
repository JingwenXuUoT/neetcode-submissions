class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_len = 0
        left = 0
        window = set()

        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left+=1
            window.add(s[right]) # each character is added once and remove dat least once
            longest_len = max(longest_len, right-left+1)

        
        return longest_len