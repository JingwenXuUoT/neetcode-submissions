class Solution:

    def encode(self, strs: List[str]) -> str:
        # input: str1, str2
        # output: len(str1)#str1len(str2)#str2
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
            # res += len(s) is not right, must to convert into a string
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0

        while start < len(s):
            # find the length prefix ending
            end = start
            while s[end] != '#':
                end+=1
            
            # extract the length of the upcoming string
            length = int(s[start:end])

            # move pointer past the '#' character
            start  = end + 1

            # Extract the actual string based on the length
            res.append(s[start: start + length])

            # Move ponter to the start of the next encoded block
            start += length

        return res