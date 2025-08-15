# Last updated: 8/15/2025, 1:40:11 PM
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 1
        bed = [0] + flowerbed + [0]

        while i < len(bed) -1 and n > 0:
            if bed[i] == 0:
                if bed[i-1] == 0 and bed[i+1] == 0:
                    bed[i] = 1
                    n -= 1
                    i += 2
                    continue
            i += 1
        return n <= 0