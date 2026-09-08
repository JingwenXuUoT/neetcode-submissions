class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        match = set()
        for tri in triplets:
            # for i in range(3):
            #     if tri[i] > target[i]:
            #         break
            #     elif tri[i] == target[i]:
            #         match.add(i)
            # the above logic cannot avoid a invalid triplet in position 1 or 2 still add index 0 or 1 to the set
            if any(tri[i] > target[i] for i in range(3)):
                continue # skip the whole triplet and have seperate logic on add operation
            for i in range(3):
                if tri[i] == target[i]:
                    match.add(i)

        return len(match) == 3
        