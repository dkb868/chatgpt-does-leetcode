"""solve in python3, just give a code block.

You are given a string s that consists of the digits '1' to '9' and two integers k and minLength.

A partition of s is called beautiful if:

s is partitioned into k non-intersecting substrings.
Each substring has a length of at least minLength.
Each substring starts with a prime digit and ends with a non-prime digit. Prime digits are '2', '3', '5', and '7', and the rest of the digits are non-prime.
Return the number of beautiful partitions of s. Since the answer may be very large, return it modulo 10^9 + 7.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "23542185131", k = 3, minLength = 2
Output: 3
Explanation: There exists three ways to create a beautiful partition:
"2354 | 218 | 5131"
"2354 | 21851 | 31"
"2354218 | 51 | 31"
Example 2:

Input: s = "23542185131", k = 3, minLength = 3
Output: 1
Explanation: There exists one way to create a beautiful partition: "2354 | 218 | 5131".
Example 3:

Input: s = "3312958", k = 3, minLength = 1
Output: 1
Explanation: There exists one way to create a beautiful partition: "331 | 29 | 58".
 

Constraints:

1 <= k, minLength <= s.length <= 1000
s consists of the digits '1' to '9'.

---

class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
"""


def is_prime(n: int) -> bool:
    if n in {2, 3, 5, 7}:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        def count_partitions(i: int, k: int, s: str, memo: Dict[Tuple[int, int, str], int]) -> int:
            if (i, k, s) in memo:
                return memo[(i, k, s)]
            if k == 0:
                return 1 if i == len(s) else 0
            if len(s) - i < k * minLength:
                return 0
            count = 0
            for j in range(i + minLength - 1, len(s)):
                if is_prime(int(s[i])) and not is_prime(int(s[j])):
                    count += count_partitions(j + 1, k - 1, s, memo)
                    count %= 10 ** 9 + 7
            memo[(i, k, s)] = count
            return count


        memo = {}
        return count_partitions(0, k, s, memo)


