"""solve in python3, just give the code block.

You are given a string s and a positive integer k.

Select a set of non-overlapping substrings from the string s that satisfy the following conditions:

The length of each substring is at least k.
Each substring is a palindrome.
Return the maximum number of substrings in an optimal selection.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "abaccdbbd", k = 3
Output: 2
Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
It can be shown that we cannot find a selection with more than two valid substrings.
Example 2:

Input: s = "adbcda", k = 2
Output: 0
Explanation: There is no palindrome substring of length at least 2 in the string.
 

Constraints:

1 <= k <= s.length <= 2000
s consists of lowercase English letters.

---

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
"""


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
        for d in range(2, n):
            for i in range(n-d):
                j = i+d
                if s[i] == s[j] and dp[i+1][j-1] == 1:
                    dp[i][j] = 1
        dp2 = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                if dp[i][j] == 1 and j-i+1 >= k:
                    dp2[i][j] = 1
        for j in range(n):
            for i in range(j):
                for p in range(i+k-1, j):
                    if dp2[i][p] and dp2[p+1][j]:
                        dp2[i][j] = max(dp2[i][j], dp2[i][p]+dp2[p+1][j])
        return max(dp2[i][j] for i in range(n) for j in range(i, n))
