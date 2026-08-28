class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        freq_s1 = [0] * 26
        freq_subs2 = [0] * 26
        for i in range(len(s1)):
            # the TC of ord() is O(1)
            freq_s1[ord(s1[i])-97] += 1
            freq_subs2[ord(s2[i])-97] += 1
        if freq_subs2 == freq_s1:
            return True
        for i in range(len(s1), len(s2)):
            freq_subs2[ord(s2[i])-97] += 1
            freq_subs2[ord(s2[i-len(s1)])-97] -= 1
            if freq_s1 == freq_subs2:
                return True
        return False