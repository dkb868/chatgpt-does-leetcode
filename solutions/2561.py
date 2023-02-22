"""You have two fruit baskets containing n fruits each. You are given two 0-indexed integer arrays basket1 and basket2 representing the cost of fruit in each basket. You want to make both baskets equal. To do so, you can use the following operation as many times as you want:

Chose two indices i and j, and swap the ith fruit of basket1 with the jth fruit of basket2.
The cost of the swap is min(basket1[i],basket2[j]).
Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.

Return the minimum cost to make both the baskets equal or -1 if impossible.

 

Example 1:

Input: basket1 = [4,2,2,2], basket2 = [1,4,1,2]
Output: 1
Explanation: Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.
Example 2:

Input: basket1 = [2,3,4,1], basket2 = [3,2,5,1]
Output: -1
Explanation: It can be shown that it is impossible to make both the baskets equal.

---

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
"""


from typing import List


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        total_cost_1 = sum(basket1)
        total_cost_2 = sum(basket2)
        
        if total_cost_1 != total_cost_2:
            diff = abs(total_cost_1 - total_cost_2)
            if diff % 2 != 0:
                return -1
            diff //= 2
            
        fruit_cost = {}
        for i in range(len(basket1)):
            fruit_cost[i] = [basket1[i], basket2[i]]
        
        sorted_fruits = sorted(fruit_cost.items(), key=lambda x: min(x[1]))
        
        cost_diff = diff
        for i in range(len(sorted_fruits)):
            idx, costs = sorted_fruits[i]
            cost1, cost2 = costs
            
            if total_cost_1 > total_cost_2:
                if cost1 <= cost2 and cost_diff >= cost1 - cost2:
                    total_cost_1 -= cost1 - cost2
                    total_cost_2 += cost1 - cost2
                    cost_diff -= cost1 - cost2
                elif cost2 < cost1 and cost_diff >= cost2 - cost1:
                    total_cost_1 += cost2 - cost1
                    total_cost_2 -= cost2 - cost1
                    cost_diff -= cost2 - cost1
            else:
                if cost2 <= cost1 and cost_diff >= cost2 - cost1:
                    total_cost_1 += cost2 - cost1
                    total_cost_2 -= cost2 - cost1
                    cost_diff -= cost2 - cost1
                elif cost1 < cost2 and cost_diff >= cost1 - cost2:
                    total_cost_1 -= cost1 - cost2
                    total_cost_2 += cost1 - cost2
                    cost_diff -= cost1 - cost2
                    
            if cost_diff <= 0:
                return diff
        
        if total_cost_1 != total_cost_2:
            return -1
        
        return diff


