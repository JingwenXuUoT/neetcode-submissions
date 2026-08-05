class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        for i in s:
            count = s_map.get(i, 0)
            s_map[i] = count + 1
    
        counter = 0
        for j in t:
            count = s_map.get(j, 0)
            if count:
                if count == 1:
                    s_map[j] = 0
                    counter = counter + 1
                else:
                    s_map[j] = count - 1
            else:
                return False

        return True