"""solve in python3, just give a code block, with no explanation.

You are given an m x n integer matrix grid and an array queries of size k.

Find an array answer of size k such that for each integer queres[i] you start in the top left cell of the matrix and repeat the following process:

If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
Otherwise, you do not get any points, and you end this process.
After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

Return the resulting array answer.

Example 1:


Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
Output: [5,8,1]
Explanation: The diagrams above show which cells we visit to get points for each query.
Example 2:


Input: grid = [[5,2,1],[1,1,2]], queries = [3]
Output: [0]
Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.
 

Constraints:
m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 10^5
k == queries.length
1 <= k <= 10^4
1 <= grid[i][j], queries[i] <= 10^6

---

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
"""


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        def dfs(x: int, y: int, target: int) -> int:
            if not (0 <= x < m and 0 <= y < n and grid[x][y] < target): 
                return 0
            if visited[x][y]: 
                return 0
            
            visited[x][y] = True
            points = 1
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                points += dfs(nx, ny, target)
            
            return points
        
        m, n = len(grid), len(grid[0])
        points = [0] * len(queries)
        for i, target in enumerate(queries):
            visited = [[False] * n for _ in range(m)]
            for x in range(m):
                for y in range(n):
                    if grid[x][y] < target:
                        points[i] += dfs(x, y, target)
        
        return points


