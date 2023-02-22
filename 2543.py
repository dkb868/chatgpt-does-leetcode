"""Solve this problem in python 3, no explanation needed.

There exists an infinitely large grid. You are currently at point (1, 1), and you need to reach the point (targetX, targetY) using a finite number of steps.

In one step, you can move from point (x, y) to any one of the following points:

(x, y - x)
(x - y, y)
(2 * x, y)
(x, 2 * y)
Given two integers targetX and targetY representing the X-coordinate and Y-coordinate of your final position, return true if you can reach the point from (1, 1) using some number of steps, and false otherwise.

 

Example 1:

Input: targetX = 6, targetY = 9
Output: false
Explanation: It is impossible to reach (6,9) from (1,1) using any sequence of moves, so false is returned.
Example 2:

Input: targetX = 4, targetY = 7
Output: true
Explanation: You can follow the path (1,1) -> (1,2) -> (1,4) -> (1,8) -> (1,7) -> (2,7) -> (4,7).

---

class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
"""


class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        if targetX < 1 or targetY < 1:
            return False
        if targetX == 1 and targetY == 1:
            return True
        if targetX > targetY:
            return self.isReachable(targetX - targetY, targetY)
        else:
            return self.isReachable(targetX, targetY - targetX)


