"""Solve in python 3

You are given a 0-indexed array of strings words and a 2D array of integers queries.

Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
Output: [2,3,0]
Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
The answer to the query [0,2] is 2 (strings "aba" and "ece").
to query [1,4] is 3 (strings "ece", "aa", "e").
to query [1,1] is 0.
We return [2,3,0].
Example 2:

Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
Output: [3,2,1]
Explanation: Every string satisfies the conditions, so we return [3,2,1].

---

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
"""


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Define a helper function to check if a string starts and ends with a vowel
        def is_vowel_string(s):
            vowels = {'a', 'e', 'i', 'o', 'u'}
            return s[0] in vowels and s[-1] in vowels


        # Build a prefix sum of the number of vowel strings up to each index
        vowel_counts = [is_vowel_string(words[i]) for i in range(len(words))]
        for i in range(1, len(vowel_counts)):
            vowel_counts[i] += vowel_counts[i-1]


        # Use the prefix sum to answer each query
        ans = []
        for query in queries:
            l, r = query
            count = vowel_counts[r] - (vowel_counts[l-1] if l > 0 else 0)
            ans.append(count)
        return ans


