from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return []

        rows, cols = len(image), len(image[0])
        col = image[sr][sc]

        # If the starting pixel already has the target color, return the image
        if col == color:
            return image

        q = deque([(sr, sc)])
        image[sr][sc] = color  # Color the starting pixel

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        while q:
            i, j = q.popleft()

            for dr, dc in directions:
                r, c = i + dr, j + dc

                if (0 <= r < rows and 0 <= c < cols) and image[r][c] == col:
                    q.append((r, c))
                    image[r][c] = color

        return image
