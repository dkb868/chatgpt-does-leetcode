"""Solve in python 3, no explanation needed.

You are given two 0-indexed binary strings s and target of the same length n. You can do the following operation on s any number of times:

Choose two different indices i and j where 0 <= i, j < n.
Simultaneously, replace s[i] with (s[i] OR s[j]) and s[j] with (s[i] XOR s[j]).
For example, if s = "0110", you can choose i = 0 and j = 2, then simultaneously replace s[0] with (s[0] OR s[2] = 0 OR 1 = 1), and s[2] with (s[0] XOR s[2] = 0 XOR 1 = 1), so we will have s = "1110".

Return true if you can make the string s equal to target, or false otherwise.

 

Example 1:

Input: s = "1010", target = "0110"
Output: true
Explanation: We can do the following operations:
- Choose i = 2 and j = 0. We have now s = "0010".
- Choose i = 2 and j = 1. We have now s = "0110".
Since we can make s equal to target, we return true.
Example 2:

Input: s = "11", target = "00"
Output: false
Explanation: It is not possible to make s equal to target with any number of operations.

---

class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
"""


class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        # We can only make s equal to target if they have the same number of 1's
        if s.count('1') != target.count('1'):
            return False
        
        n = len(s)
        # We can't change a bit that's already equal to the target
        # So, we need to ignore those bits by setting them to '0' in both strings
        for i in range(n):
            if s[i] == target[i]:
                s = s[:i] + '0' + s[i+1:]
                target = target[:i] + '0' + target[i+1:]
        
        # We can make s equal to target if s and target have the same bitwise OR
        # We can use a bitwise OR mask to check if s and target have the same OR
        or_mask = int(s, 2) | int(target, 2)
        return s == target or (int(s, 2) | or_mask) == or_mask


