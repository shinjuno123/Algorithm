class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        init_color = image[sr][sc]
        max_row = len(image) - 1
        max_col = len(image[sr]) - 1

        def fill(row, col):
            if row < 0 or col < 0 or row > max_row or col > max_col or image[row][col] == color or image[row][col] != init_color:
                return

            image[row][col] = color
            fill(row, col + 1) # move top
            fill(row, col - 1) # move down
            fill(row + 1, col) # move right
            fill(row - 1, col) # move left


        fill(sr, sc)

        return image