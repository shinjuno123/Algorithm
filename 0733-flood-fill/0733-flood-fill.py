class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        init_color = image[sr][sc]
        if init_color == color:
            return image
        max_r, max_c = len(image) - 1, len(image[0]) - 1

        def fill(r, c):
            if r < 0 or r > max_r or c < 0 or c > max_c or image[r][c] != init_color:
                return
            
            image[r][c] = color
            fill(r + 1, c)
            fill(r - 1, c)
            fill(r, c + 1)
            fill(r, c - 1)

        fill(sr, sc)
        return image


        # old = image[sr][sc]
        # if old == color:
        #     return image

        # m = len(image)
        # n = len(image[0])

        # def dfs(i, j):
        #     if i < 0 or i >= m or j < 0 or j >= n or image[i][j] != old:
        #         return
        #     image[i][j] = color
        #     dfs(i+1, j)
        #     dfs(i-1, j)
        #     dfs(i, j + 1)
        #     dfs(i, j - 1)
        
        # dfs(sr, sc)
        # return image