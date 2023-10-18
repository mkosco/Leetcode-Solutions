class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        num_placed = 0
        for i in range(len(flowerbed)):
            if i == 0:
                if len(flowerbed) > 1 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    num_placed += 1
                    continue
                elif len(flowerbed) == 1 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    num_placed += 1
                    continue
                else:
                    continue

            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and i != (len(flowerbed) - 1) and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                num_placed += 1

            if i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                num_placed += 1

        return num_placed >= n