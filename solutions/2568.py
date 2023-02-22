"""You are given a 0-indexed integer array nums.

We say that an integer x is expressible from nums if there exist some integers 0 <= index1 < index2 < ... < indexk < nums.length for which nums[index1] | nums[index2] | ... | nums[indexk] = x. In other words, an integer is expressible if it can be written as the bitwise OR of some subsequence of nums.

Return the minimum positive non-zero integer that is not expressible from nums.

 

Example 1:

Input: nums = [2,1]
Output: 4
Explanation: 1 and 2 are already present in the array. We know that 3 is expressible, since nums[0] | nums[1] = 2 | 1 = 3. Since 4 is not expressible, we return 4.
Example 2:

Input: nums = [5,3,2]
Output: 1
Explanation: We can show that 1 is the smallest number that is not expressible.

---

class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
"""


class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        max_num = max(nums)
        possible_sums = set([0])
        for num in nums:
            new_sums = set()
            for possible_sum in possible_sums:
                new_sums.add(possible_sum | num)
            possible_sums |= new_sums
        for i in range(1, max_num + 2):
            if i not in possible_sums:
                return i

