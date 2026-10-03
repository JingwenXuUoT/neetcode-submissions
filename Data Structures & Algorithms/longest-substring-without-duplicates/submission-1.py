class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_len = 0
        left = 0
        window = set()

        for right in range(len(s)):
            while s[right] in window: # left pointer should conditionally moved
                window.remove(s[left])
                left+=1
            window.add(s[right]) # exploring pointer should blindly add
            longest_len = max(longest_len, right-left+1)

        
        return longest_len