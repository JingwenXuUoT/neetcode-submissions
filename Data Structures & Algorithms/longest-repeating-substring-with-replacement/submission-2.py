class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left = 0
        window = {}
        max_ch_len = 0

        for right in range(len(s)):
            window[s[right]]=window.get(s[right],0)+1
            
            max_ch_len = max(max_ch_len, window[s[right]])

            # The rest_total_length is alwyas linked to the siz eof the window
            while(right-left+1) - max_ch_len > k:
                window[s[left]] -= 1
                left+=1
            
            longest = max(longest, right-left+1)

        return longest