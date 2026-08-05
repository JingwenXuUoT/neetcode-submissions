class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        letter_index = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm': 12, 'n': 13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25} # optional
        for str in strs:
            counts = [0] * 26
            for letter in str:
                idx = letter_index[letter]
                # or: idx = ord(letter) - ord('a')
                counts[idx] += 1
            key = tuple(counts) # tuple is the hashable version of list
            # if anagram_map[key] != None:
            if key not in anagram_map:
                anagram_map[key]= []
            anagram_map[key].append(str) # this should not in else tier, otherwise the first str of every new group will be dropped
        
        res = []
        for key, value in anagram_map.items():
            res.append(value)
        
        return res