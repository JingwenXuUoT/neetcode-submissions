class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        hand.sort()
        freq_map = defaultdict(int)
        for h in hand:
            freq_map[h] += 1
        
        # the minimum value should be the starting value of the group
        for h in hand:
            if freq_map[h] != 0:
                # new group start from the fist still remaning smallest value
                for h_inGroup in range(h, h+groupSize):
                    if freq_map[h_inGroup] == 0:
                        return False
                    freq_map[h_inGroup] -= 1
        return True
