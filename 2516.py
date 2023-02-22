"""solve in python3, just give the code block

You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

 

Example 1:

Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation: 
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.
Example 2:

Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'b' or 'c' so return -1.

---

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
"""


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        freq = [0] * 3  # frequency of each character
        for c in s:
            freq[ord(c) - ord('a')] += 1
        
        if any(f < k for f in freq):
            return -1  # there's at least one character that can't reach k
        
        # find the shortest substring that contains k instances of each character
        i, j = 0, n - 1
        while i < j and freq[0] > k:
            if s[i] == 'a':
                freq[0] -= 1
            elif s[j] == 'a':
                freq[0] -= 1
            i += 1
            j -= 1
        while i < j and freq[2] > k:
            if s[i] == 'c':
                freq[2] -= 1
            elif s[j] == 'c':
                freq[2] -= 1
            i += 1
            j -= 1
        
        # compute the minimum number of minutes needed to take k of each character
        res = j - i + 1
        for c in s[i:j+1]:
            if freq[1] == k:
                break
            if c == 'b':
                freq[1] += 1
                res += 1
        
        return res


