class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left = 0
        window = defaultdict(int) # count the number of characters in each window, to match to the most common character
        # window = {}
        max_ch_len = 0

        for right in range(len(s)):
            # window[s[right]]=window.get(s[right],0)+1
            window[s[right]]+=1 # no such big diff
            
            max_ch_len = max(max_ch_len, window[s[right]]) # instead of using max(window.values()) to iterate over the whole map, comparing two numbers is much faster, improve from 80-84ms to 48-52 ms
            # max_ch_len = max(window.values())

            # The rest_total_length is alwyas linked to the size of the window
            # the number of characters that different from the most frequent one should be bounded by k
            while(right-left+1) - max_ch_len > k:
                window[s[left]] -= 1
                left+=1
            
            # after while, the window is valid
            longest = max(longest, right-left+1)

        return longest