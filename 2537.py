"""Solve in python 3, no explanation needed.

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if it there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1,1,1], k = 10
Output: 1
Explanation: The only good subarray is the array nums itself.
Example 2:

Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.

---

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
"""


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            freq = {}
            for j in range(i, len(nums)):
                freq[nums[j]] = freq.get(nums[j], 0) + 1
                for val in freq.values():
                    if val >= k:
                        count += 1
        return count


