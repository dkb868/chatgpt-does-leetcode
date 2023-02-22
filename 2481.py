"""solve in python3, just give a code block.

A valid cut in a circle can be:
- A cut that is represented by a straight line that touches two points on the edge of the circle and passes through its center, or
- A cut that is represented by a straight line that touches one point on the edge of the circle and its center.

Given the integer n, return the minimum number of valid cuts needed to divide a circle into n equal slices.

Example 1:

Input: n = 4
Output: 2
Explanation: 
Cutting the circle twice through the middle divides it into 4 equal slices.
Example 2:


Input: n = 3
Output: 3
Explanation:
At least 3 cuts are needed to divide the circle into 3 equal slices. 
It can be shown that less than 3 cuts cannot result in 3 slices of equal size and shape.
Also note that the first cut will not divide the circle into distinct parts.
 

Constraints:

1 <= n <= 100

---

class Solution:
    def numberOfCuts(self, n: int) -> int:
"""


import math


class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n % 2 == 1:
            k = (n - 1) // 2
            lines = [0]
            for i in range(k):
                lines.append((lines[-1] + 360 / n) % 360)
        else:
            k = math.ceil(math.log2(n / 4)) + 1
            angle = 180 * (n - 2) / n
            start = angle / 2
            lines = [start]
            for i in range(k - 1):
                angle += 180 * (n - 2) / n
                start = (start + angle) % 360
                lines.append(start)
        count = len(lines)
        for i in range(count):
            for j in range(i + 1, count):
                if abs(lines[i] - lines[j]) <= 180 / n:
                    count += 1
        return count


