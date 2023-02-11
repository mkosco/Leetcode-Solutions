class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color or sr > len(image) - 1 or sc > len(image[0]) - 1 or sr < 0 or sc < 0:
            return image
        else:
            current = image[sr][sc]
            image[sr][sc] = color

            #up
            if not sr - 1 < 0 and image[sr - 1][sc] == current:
                self.floodFill(image, sr - 1, sc, color)
            #down
            if not sr + 1 > len(image) - 1 and image[sr + 1][sc] == current:
                self.floodFill(image, sr + 1, sc, color)
            #left
            if not sc - 1 < 0 and image[sr][sc - 1] == current:
                self.floodFill(image, sr, sc - 1, color)
            #right
            if not sc + 1 > len(image[0]) - 1 and image[sr][sc + 1] == current:
                self.floodFill(image, sr, sc + 1, color)

            return image