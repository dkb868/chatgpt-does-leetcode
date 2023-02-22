"""solve in python3, just give a code block.

Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:

Append the character '0' zero times.
Append the character '1' one times.
This can be performed any number of times.

A good string is a string constructed by the above process having a length between low and high (inclusive).

Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 10^9 + 7.


Example 1:

Input: low = 3, high = 3, zero = 1, one = 1
Output: 8
Explanation: 
One possible valid good string is "011". 
It can be constructed as follows: "" -> "0" -> "01" -> "011". 
All binary strings from "000" to "111" are good strings in this example.
Example 2:

Input: low = 2, high = 3, zero = 1, one = 2
Output: 5
Explanation: The good strings are "00", "11", "000", "110", and "011".
 

Constraints:

1 <= low <= high <= 10^5
1 <= zero, one <= low

---

class Solution:
  def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
"""


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        
        # Memoization table for count(i, z, o)
        memo = {}
        
        def count(i, z, o):
            if i == 0:
                return 1
            if z == 0 and o == 0:
                return 1
            if z == 0:
                return count(i-1, z, o-1)
            if o == 0:
                return count(i-1, z-1, o)
            if (i, z, o) in memo:
                return memo[(i, z, o)]
            ans = (count(i-1, z-1, o) + count(i-1, z, o-1)) % MOD
            memo[(i, z, o)] = ans
            return ans
        
        # Compute answer by summing up count(i, z, o) for all valid i, z, o
        ans = 0
        for i in range(low, high+1):
            for z in range(1, zero+1):
                for o in range(1, one+1):
                    ans = (ans + count(i, z, o)) % MOD
        return ans


