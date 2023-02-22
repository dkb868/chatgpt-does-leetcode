"""Solve in python 3.

You are given a 0-indexed m x n binary matrix grid. You can move from a cell (row, col) to any of the cells (row + 1, col) or (row, col + 1) that has the value 1. The matrix is disconnected if there is no path from (0, 0) to (m - 1, n - 1).

You can flip the value of at most one (possibly none) cell. You cannot flip the cells (0, 0) and (m - 1, n - 1).

Return true if it is possible to make the matrix disconnect or false otherwise.

Note that flipping a cell changes its value from 0 to 1 or from 1 to 0.

 

Example 1:


Input: grid = [[1,1,1],[1,0,0],[1,1,1]]
Output: true
Explanation: We can change the cell shown in the diagram above. There is no path from (0, 0) to (2, 2) in the resulting grid.
Example 2:


Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: false
Explanation: It is not possible to change at most one cell such that there is not path from (0, 0) to (2, 2).

---

class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
"""


class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        ones = sum(sum(row) for row in grid)
        visited = set()


        def is_disconnected(matrix):
            visited.clear()
            queue = [(0, 0)]
            visited.add((0, 0))
            while queue:
                r, c = queue.pop(0)
                if r == m - 1 and c == n - 1:
                    return False
                for nr, nc in ((r+1,c), (r,c+1), (r-1,c), (r,c-1)):
                    if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] == 1 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return True


        if ones > 1:
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 0:
                        grid[r][c] = 1
                        if is_disconnected(grid):
                            return True
                        grid[r][c] = 0


        return False


