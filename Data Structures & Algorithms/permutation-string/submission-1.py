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
            # sequence comparison:
            # first, memory reference check, if the same return True
            # then, length comparison check, if not the same, return False
            # after that, element-by-element evaluation, python iterates through both lists simutaneously using their indices. The moment Python finds any index where the two values are not equal, it stops the check and return False; otherwise, return True at the end
            return True
        # sliding on s2
        for i in range(len(s1), len(s2)):
            freq_subs2[ord(s2[i])-97] += 1
            freq_subs2[ord(s2[i-len(s1)])-97] -= 1
            if freq_s1 == freq_subs2:
                return True
        return False

# comparing to "freq1==freq2" check, it's not necessary and less commonly used for maintaning a matches variable
# freq1 == freq2, has less if/else overhead, and fully executed in C code