class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k : is the eating rate -> bananas / hour

        # find the max value:
        sorted_piles = sorted(piles)
        max_val = sorted_piles[-1]

        res = max_val

        left = 1
        right = max(piles)

        while left <= right:
            k = (left + right) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = min(res, k)
                right = k - 1
            else:
                left = k + 1

        return res

