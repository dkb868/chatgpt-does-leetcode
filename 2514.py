"""solve using python3, just return a code block.

You are given a string s containing one or more words. Every consecutive pair of words is separated by a single space ' '.

A string t is an anagram of string s if the ith word of t is a permutation of the ith word of s.

For example, "acb dfe" is an anagram of "abc def", but "def cab" and "adc bef" are not.
Return the number of distinct anagrams of s. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: s = "too hot"
Output: 18
Explanation: Some of the anagrams of the given string are "too hot", "oot hot", "oto toh", "too toh", and "too oht".
Example 2:

Input: s = "aa"
Output: 1
Explanation: There is only one anagram possible for the given string.

---

class Solution:
    def countAnagrams(self, s: str) -> int:
"""


class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = int(1e9 + 7)
        words = s.split()
        n = len(words)
        freq = [{} for _ in range(n)]
        for i in range(n):
            for ch in words[i]:
                freq[i][ch] = freq[i].get(ch, 0) + 1
        ans = 1
        for i in range(n - 1):
            new_freq = {}
            for ch in words[i + 1]:
                new_freq[ch] = new_freq.get(ch, 0) + 1
            if freq[i] == new_freq:
                ans += 1
        return ans % MOD


