class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0, 0, 0]

        for t in triplets:
            valid = True
            for i in range(3):
                if t[i] > target[i]:
                    valid = False
            
            if valid:
                for i in range(3):
                    res[i] = max(res[i], t[i])

        return res == target