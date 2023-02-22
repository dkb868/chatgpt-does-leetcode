"""solve in python3, just give me a code block.

You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
Example 2:

Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.
 

Constraints:

1 <= k <= nums.length <= 10^5
1 <= nums[i] <= 10^5

---

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
"""


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Initialize the window and the set
        window = nums[:k]
        s = set(window)
        max_sum = sum(window)
        
        # Slide the window over the array
        for i in range(k, len(nums)):
            # Add the new element to the window and the set
            window.append(nums[i])
            s.add(nums[i])
            
            # Remove the leftmost element from the window and the set
            left = i - k
            s.remove(nums[left])
            window.pop(0)
            
            # Check if the window contains distinct elements
            if len(s) == k:
                # Calculate the sum of the subarray and update the maximum sum seen so far
                subarray_sum = sum(window)
                max_sum = max(max_sum, subarray_sum)
                
        return max_sum


