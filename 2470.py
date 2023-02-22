"""solve in python3, just give the code block.

Given an integer array nums and an integer k, return the number of subarrays of nums where the least common multiple of the subarray's elements is k.

A subarray is a contiguous non-empty sequence of elements within an array.

The least common multiple of an array is the smallest positive integer that is divisible by all the array elements.

 

Example 1:

Input: nums = [3,6,2,7,1], k = 6
Output: 4
Explanation: The subarrays of nums where 6 is the least common multiple of all the subarray's elements are:
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
Example 2:

Input: nums = [3], k = 2
Output: 0
Explanation: There are no subarrays of nums where 2 is the least common multiple of all the subarray's elements.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i], k <= 1000

---

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
"""


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        def lcm(a: int, b: int) -> int:
            return a * b // gcd(a, b)

        left = 0
        res = 0
        curr_lcm = 1
        for right, num in enumerate(nums):
            curr_lcm = lcm(curr_lcm, num)
            while curr_lcm > k and left <= right:
                curr_lcm //= nums[left]
                left += 1
            if curr_lcm == k:
                res += right - left + 1
        return res
