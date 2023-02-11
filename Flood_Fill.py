class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color or sr > len(image) - 1 or sc > len(image[0]) - 1 or sr < 0 or sc < 0:
            return image
        else:
            image[sr][sc] = color

            #up
            self.floodFill(image, sr - 1, sc, color)
            #down
            self.floodFill(image, sr + 1, sc, color)
            #left
            self.floodFill(image, sr, sc - 1, color)
            #right
            self.floodFill(image, sr, sc + 1, color)

            return image