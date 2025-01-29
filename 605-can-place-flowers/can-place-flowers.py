class Solution(object):
    # [1, 0, 0, 0, 1] n = 1
    # [1, 0, 1, 0, 1] true

    # [1, 0, 0, 0, 1] n = 2
    # [1, 0, 1, 0, 1] false

    # [0, 1, 0, 0, 0, 0, 1, 0] n = 3
    # [0, 1, 0, 1, 0, 0, 1, 0] false
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        elif len(flowerbed) < 1:
            return False

        available_spots = 0

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            available_spots += 1
            flowerbed[0] = 1

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                available_spots += 1
                flowerbed[i] = 1

        if flowerbed[len(flowerbed) - 1] == 0 and flowerbed[len(flowerbed) - 2] == 0:
            available_spots += 1
            flowerbed[len(flowerbed) - 1] = 1

        return available_spots >= n
