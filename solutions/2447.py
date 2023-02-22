"""solve in python3, just give a code block.

Given an integer array nums and an integer k, return the number of subarrays of nums where the greatest common divisor of the subarray's elements is k.

A subarray is a contiguous non-empty sequence of elements within an array.

The greatest common divisor of an array is the largest integer that evenly divides all the array elements.

 

Example 1:

Input: nums = [9,3,1,2,6,3], k = 3
Output: 4
Explanation: The subarrays of nums where 3 is the greatest common divisor of all the subarray's elements are:
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
Example 2:

Input: nums = [4], k = 7
Output: 0
Explanation: There are no subarrays of nums where 7 is the greatest common divisor of all the subarray's elements.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i], k <= 10^9

---

class Solution:
  def subarrayGCD(self, nums: List[int], k: int) -> int:
"""


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)


        divisors = []
        for i in range(1, int(k**0.5) + 1):
            if k % i == 0:
                divisors.append(i)
                if i != k // i:
                    divisors.append(k // i)


        count = 0
        n = len(nums)
        for divisor in divisors:
            subarray_gcd = 0
            for i in range(n):
                subarray_gcd = gcd(subarray_gcd, nums[i])
                if subarray_gcd == divisor:
                    count += n - i
                    break


        return count


